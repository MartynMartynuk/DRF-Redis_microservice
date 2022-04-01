from rest_framework.serializers import ModelSerializer
from microservice.models import Devices


class DevicesSerializer(ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

    def create(self, validated_data):
        return Devices.objects.create(**validated_data)
