__author__ = 'Da Vinci'
from django.urls import path
from Adverts import views

urlpatterns = [
    path('images/',views.ImageAd.as_view()),
    path('gif/',views.GifAd.as_view()),
    path('videos/',views.VideoAd.as_view()),
]