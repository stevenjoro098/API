__author__ = 'Da Vinci'
from rest_framework import serializers
from Adverts.models import ImageAdverts, VideosAdverts, GifAdverts

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','ad_priority','advert_image')
        model = ImageAdverts
class VideoAdsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','ad_priority','video_url',)
        model = VideosAdverts
class GifSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','ad_priority','gif_url',)
        model = GifAdverts