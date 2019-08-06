__author__ = 'Da Vinci'
from django.urls import path
from NewsRoom import views

urlpatterns = [
    path('',views.NewsList.as_view()),
    path('<int:pk>/', views.NewsDetails.as_view()),
]