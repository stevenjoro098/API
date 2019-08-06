__author__ = 'Da Vinci'
from django.urls import path
from Music import views

urlpatterns = [
    path('',views.MusicList.as_view()),
    path('<int:pk>/', views.MusicDetail.as_view()),
]