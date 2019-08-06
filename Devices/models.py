from django.db import models

# Create your models here.
class Devices(models.Model):
    device_name = models.CharField(max_length = 250)
    device_slug = models.SlugField(max_length = 250,unique=True)
    token_value = models.CharField(max_length = 250,blank=True)
    device_status = models.BooleanField(default=False)
    longitude = models.FloatField(max_length = 250)
    latitude = models.FloatField(max_length = 250)

    def __str__(self):
        return self.device_name