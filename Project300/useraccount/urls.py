from django.urls import path

from .import views

urlpatterns = [
    path('', views.reg, name='register') 
]