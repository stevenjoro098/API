__author__ = 'Da Vinci'
from rest_framework import serializers
from Music.models import Music

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title','image_url', 'artist', 'album', 'genre','play','music_file')
        model = Music
