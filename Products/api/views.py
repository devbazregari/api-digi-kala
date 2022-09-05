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
        sold_product  =     Sold(count = 1)
        product       =     Product(**request.data[0]  , product_sold_id_fk = sold_product)
        prod_category =     Category(name=category, product_id_fk=product)

        sold_product.save()
    
        attr.save()
        product.save()
        prod_category.save()
        product.attrs.add(attr)
        return Response("product saved ")


class SearchListView(generics.ListAPIView):

    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['intro', 'title']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
      
        return context





# class MostSeenListView(generics.ListAPIView):


#     seens = Seen.objects.order_by('seen').filter(seen=1)
#     # queryset = Product.objects.filter(product_id__in = [i.prod_id_fk.pk for i in seens])
    

#     # seens  = [i for i in Seen.objects.values_list('prod_id_fk_id','seen').distinct()]
    
#     print(seens)
    


#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context["user_id"] = self.request.user.id
      
#         return context

    

    