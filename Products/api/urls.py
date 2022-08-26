from django.urls import path 
from .views import create , test



urlpatterns = [
    
    path('create', create  , name='create'),
    path('test/<int:pk>', test  , name='test'),
   
   

]
