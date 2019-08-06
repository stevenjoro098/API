__author__ = 'Da Vinci'
from django.urls import path
from Devices import views

urlpatterns = [
    path('',views.DeviceList.as_view()),
    path('<int:pk>/', views.DeviceDetail.as_view()),
]