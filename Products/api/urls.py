from django.urls import path 
from .views import  CreateProductListView , SearchListView , SellProduct , MostSeenProductListView , MostSeenListView , SuggestProductListView , UserProducts



urlpatterns = [
    
        path('list', SearchListView.as_view()  , name='search'),
        path('user_product', UserProducts.as_view()  , name='user_product'),
        path('most/<str:type>/<str:category>' , MostSeenListView.as_view() , name='most_seen'),
        path('most_seen/<str:category>' , MostSeenProductListView.as_view() , name='most_seen'),
        path('suggest' , SuggestProductListView.as_view() , name='suggest'),
        path('sell/<int:pk>/<int:price>' , SellProduct.as_view() , name='sell' ),
        path('create', CreateProductListView.as_view() , name='create'),
   

]
