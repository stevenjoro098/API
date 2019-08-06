__author__ = 'Da Vinci'
from django.urls import path
from Movies import views

urlpatterns = [
    path('',views.MoviesList.as_view()),
    path('<int:pk>/', views.MoviesDetail.as_view()),
]