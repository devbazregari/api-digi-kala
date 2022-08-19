
from django.contrib import admin
from django.urls import path 
from .views import  UserLoginListCreateAPIView , UserRegister
urlpatterns = [



    # API URL 

    path('login',  UserLoginListCreateAPIView.as_view() , name='login' ),
    path('register',  UserRegister.as_view() , name='list' ),
    
]
