from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Products.models import Attr, Product, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from User.models import User
from .serializers import ProductSerializer
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CreateProductListView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        product = Product(**request.data[0])
        attr = Attr(**request.data[1])
        category = request.data[0].pop('category')
        prod_category = Category(name=category, product_id_fk=product)

        attr.save()
        product.save()
        prod_category.save()
        product.attrs.add(attr)
        return Response("product saved ")


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['intro', 'title']

    # def get(self, request, *args, **kwargs):

    #     category = Category.objects.select_related('product_id_fk').filter(name__contains='laptop')

    #     print(category)
    #     for i in category:
    #         print(i.name)
    #         print(i.product_id_fk.title)

    #     return Response({'hi':'there'})
