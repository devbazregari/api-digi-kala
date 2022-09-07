from ast import List, arg
from itertools import product
from unicodedata import category
from rest_framework.response import Response
from Products.models import Attr, Product, Category, Sold , Seen
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer 
from rest_framework import generics
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Max , Count
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

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


class SearchListView( generics.ListAPIView):

    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['intro', 'title','category_id_fk_id__name']




    def get_serializer_context(self , **kwargs):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
      
        return context


   


class SellProduct(APIView):

    def get(self , request , **kwargs):

        product_id  = Product.objects.get(pk=kwargs['pk'])
        price       = kwargs['price']
        user_bought = request.user

        sold_obj    = Sold(sold=price ,prod_id_fk = product_id , user_id_fk = user_bought , category = product_id.category_id_fk)
        sold_obj.save()
    
        return Response('product registered to products sold ')


class MostSeenListView(mixins.ListModelMixin , generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    pagination_class = PageNumberPagination

    filter_backends = [SearchFilter , OrderingFilter,]  
    search_fields = ['intro', 'title']

    def get_queryset(self ):

        print(self.kwargs)
        return Sold.get_queries(self.kwargs)




    def get(self, request, *args, **kwargs):
        
        return self.list(request,*args , **kwargs)
    
    def get_serializer_context(self , **kwargs):
        context = super().get_serializer_context()

        context["user_id"] = self.request.user.id
        context["param"] = self.kwargs['category']

      
        return context






















# class MostSeenListView(generics.ListAPIView):

#     seens = Seen.objects.order_by('seen').filter(last='True')[0:1]
#     queryset = Product.objects.filter(product_id__in = [i.prod_id_fk.pk for i in seens])
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProductSerializer

#     filter_backends = [SearchFilter, DjangoFilterBackend]
#     search_fields = ['category_id_fk_id__name']
    
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context["user_id"] = self.request.user.id
      
#         return context



# class SellListView(generics.ListCreateAPIView):

#     def post(self, request, *args, **kwargs):
        
        
        


#         return Response('hi')
    

    