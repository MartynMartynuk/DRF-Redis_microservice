import random
import redis
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from drf_redis_microservice.settings import REDIS_HOST, REDIS_PORT
from microservice.models import Devices
from microservice.serializers import DevicesSerializer


class DevicesAPIView(ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    dev_type_list = ['emeter', 'zigbee', 'lora', 'gsm']

    def list(self, request, *args, **kwargs):
        if request.data.get('sort') is not None:
            sorted_list = []
            for item in self.dev_type_list:
                devices = Devices.objects.filter(dev_type=item, endpoint=None)
                if len(list(devices)) != 0:
                    sorted_list.append(DevicesSerializer(devices, many=True).data)
            return Response(sorted_list)
        else:
            devices = Devices.objects.all()
            return Response({'devices': DevicesSerializer(devices, many=True).data})

    def create(self, request, *args, **kwargs):
        if request.data.get('add_10') is not None:
            dev_id = self.random_adder()
            self.endpoint_adder(dev_id)
            return Response(status=201)
        else:
            serializer = DevicesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=200)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method DELETE not allowed'})
        try:
            instance = Devices.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = DevicesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"device": serializer.data})

    @staticmethod
    def randomMAC():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    @staticmethod
    def random_adder():
        dev_type = []
        dev_id = []
        for i in range(0, 10):
            dev_type.append(DevicesAPIView.dev_type_list[random.randint(0, 3)])
            dev_id.append(DevicesAPIView.randomMAC())
            requests.post('http://127.0.0.1:8000/api/devices/',
                          json={'dev_type': dev_type[i], 'dev_id': dev_id[i]})
        return dev_id

    @staticmethod
    def endpoint_adder(dev_id):
        endpoints = random.sample(dev_id, 5)
        print(endpoints)


redis_instance = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)


@api_view(['POST'])
def redis_counter(request):
    if request.method == 'POST':
        counter = int(redis_instance.get('counter'))
        word_1 = request.data.get('word_1')
        word_2 = request.data.get('word_2')
        if sorted(word_1) == sorted(word_2):
            counter += 1
            redis_instance.set('counter', counter)
            return Response({'is_anagram': True, 'counter': redis_instance.get('counter')})
        else:
            return Response({'is_anagram': False, 'counter': redis_instance.get('counter')})
