__author__ = 'Da Vinci'
from rest_framework import serializers
from NewsRoom.models import NewsRoom

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title','image_url', 'events', 'location')
        model = NewsRoom
