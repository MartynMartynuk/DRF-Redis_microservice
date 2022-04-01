from django.db import models


class Devices(models.Model):
    dev_type = models.CharField(max_length=7)
    dev_id = models.CharField(primary_key=True, max_length=17)
    endpoint = models.ForeignKey('Endpoints', on_delete=models.PROTECT, null=True)


class Endpoints(models.Model):
    endpoint_field = models.IntegerField()
