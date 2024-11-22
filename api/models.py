from django.db import models


class DataRecord(models.Model):
    ne = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    gsm = models.BooleanField()
    umts = models.BooleanField()
    lte = models.BooleanField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.ne
