from django.urls import path 
from .views import register , login
from rest_framework.authtoken import views





urlpatterns = [

    path('login', login , name='login' ),
    
    path('register', register , name='register'),



]
