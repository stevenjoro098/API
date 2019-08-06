from rest_framework import generics
from Movies.models import Movies
from Movies.serializers import MoviesSerializer
# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer