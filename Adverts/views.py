from django.shortcuts import render
from  rest_framework import generics
from Adverts.models import GifAdverts,VideosAdverts,ImageAdverts
# Create your views here.
from Adverts.serializers import ImagesSerializer,VideoAdsSerializer,GifSerializer
class ImageAd(generics.ListAPIView):
    queryset = ImageAdverts.objects.all()
    serializer_class = ImagesSerializer

class VideoAd(generics.ListAPIView):
    queryset = VideosAdverts.objects.all()
    serializer_class = VideoAdsSerializer

class GifAd(generics.ListAPIView):
    queryset = GifAdverts.objects.all()
    serializer_class = GifSerializer
