from rest_framework import generics
from Devices.models import Devices
from Devices.serializers import DevicesSerializer
# Create your views here.

class DeviceList(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer