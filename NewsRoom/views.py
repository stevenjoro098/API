from rest_framework import generics
from NewsRoom.models import NewsRoom
from NewsRoom.serializer import NewsSerializer
# Create your views here.

class NewsList(generics.ListAPIView):
    queryset = NewsRoom.objects.all()
    serializer_class = NewsSerializer

class NewsDetails(generics.RetrieveAPIView):
    queryset = NewsRoom.objects.all()
    serializer_class =  NewsSerializer