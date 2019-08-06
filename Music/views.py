from rest_framework import generics
from Music.models import Music
from Music.serializers import MusicSerializer
# Create your views here.

class MusicList(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
