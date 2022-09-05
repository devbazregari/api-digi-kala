from rest_framework.response import Response
from Products.models import Attr, Product, Category, Sold
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from rest_framework import generics
from django.utils import timezone
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


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

    
    print(timezone.now())
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['intro', 'title']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
      
        return context
