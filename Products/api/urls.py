from django.urls import path 
from .views import  CreateProductListView , SearchListView , MostSeenListView



urlpatterns = [
    
        path('list', SearchListView.as_view()  , name='search'),
        path('most-seen', MostSeenListView.as_view()  , name='most-seen'),
#     path('sell' , SellListView.as_view() , name='sell' ),
        path('create', CreateProductListView.as_view() , name='create'),
   

]
