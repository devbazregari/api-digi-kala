from django.urls import path 
from .views import register 
from rest_framework.authtoken import views




urlpatterns = [
    
    path('register', register , name='register'),
    path('login', views.obtain_auth_token ),


]
