__author__ = 'Da Vinci'
from rest_framework import serializers
from Movies.models import Movies

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id',
                  'image_url',
                  'title',
                  'category',
                  'star_ratings',
                  'plot',
                  'year',
                  'website',
                  'movie_url',
                  'slug',
                  'views')
        model = Movies