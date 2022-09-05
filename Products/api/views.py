from itertools import product
from rest_framework.response import Response
from Products.models import Attr, Product, Category, Sold , Seen
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer 
from rest_framework import generics
from django.utils import timezone
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Max 


class CreateProductListView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        
        attr          =     Attr(**request.data[1])
        category      =     request.data[0].pop('category')

        category_obj  =     Category.objects.get_or_create(name=category)

        product       =     Product(**request.data[0] , category_id_fk = category_obj[0])



    
        attr.save()
     
        product.save()
        product.attrs.add(attr)
        return Response("product saved ")


class SearchListView(generics.ListAPIView):

    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['intro', 'title','category']

    def get_serializer_context(self , **kwargs):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
      
        return context


class MostSeenListView(generics.ListAPIView):

    seens = Seen.objects.order_by('seen').filter(last='True')[0:1]
    queryset = Product.objects.filter(product_id__in = [i.prod_id_fk.pk for i in seens])
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['category_id_fk__name']
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
      
        return context



# class SellListView(generics.ListCreateAPIView):

#     def post(self, request, *args, **kwargs):
        
        
        


#         return Response('hi')
    

    