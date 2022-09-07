from django.urls import path 
from .views import  CreateProductListView , SearchListView , SellProduct  , MostSeenListView



urlpatterns = [
    
        path('list', SearchListView.as_view()  , name='search'),
        path('most/<str:type>/<str:category>' , MostSeenListView.as_view() , name='most_seen'),
        path('sell/<int:pk>/<int:price>' , SellProduct.as_view() , name='sell' ),
        path('create', CreateProductListView.as_view() , name='create'),
   

]
