from rest_framework import serializers
from Products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title','brand','price','mainImage','brandCategory','intro','overView']

