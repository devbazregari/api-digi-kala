from django.urls import path 
from .views import  SearchListView , CreateProductListView 



urlpatterns = [
    
    path('list', SearchListView.as_view()  , name='search'),
    # path('most-seen', MostSeenListView.as_view()  , name='most-seen'),
   
    path('create', CreateProductListView.as_view() , name='create'),
   

]
