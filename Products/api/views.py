
from rest_framework.response import Response
from Products.models import Attr, Product, Category, Sold , Seen
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count , Q
from rest_framework import mixins
from datetime import datetime
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

        DISCOUNT = False
        product_id  = Product.objects.get(pk=kwargs['pk'])
        price       = kwargs['price']
        user_bought = request.user

        today = datetime.today()
        year  = datetime(today.year, today.month, 1)

        year , month = str(datetime.today().year) , str(datetime.today().month)

        time_now = year + "-" + "0"+month if len(month) == 1 else month


        
        discount = Sold.objects.filter(user_id_fk_id=user_bought.pk , created_on__startswith=time_now , discount=True)
        
        
        
        product_user_bought = Sold.objects.annotate(count=Count('user_id_fk_id')).filter(user_id_fk_id=user_bought.pk , created_on__startswith=time_now)

        
        print(product_user_bought)

        print(discount)
        print('discount')
        
        if not discount:
            if len(product_user_bought) >= 2 :
                price = int((price /100 ) * 30)
                DISCOUNT = True

        print(price)
        sold_obj    = Sold(sold=price ,prod_id_fk = product_id , user_id_fk = user_bought , category_id_fk = product_id.category_id_fk , discount=DISCOUNT)
        sold_obj.save()
    
        return Response('product registered to products sold ')


class MostSeenListView(mixins.ListModelMixin , generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    pagination_class = PageNumberPagination

    
   

    def get_queryset(self ):

        return Sold.get_queries(self.kwargs)




    def get(self, request, *args, **kwargs):
        
        return self.list(request,*args , **kwargs)
    
    def get_serializer_context(self , **kwargs):
        context = super().get_serializer_context()

        context["user_id"] = self.request.user.id
        context["param"] = self.kwargs['category']

      
        return context



class MostSeenProductListView(generics.ListAPIView):


    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer



    def get_queryset(self):
        return Seen.get_most_seen_product(self.kwargs)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
        context["param"] = self.kwargs['category']
        return context



# class SellListView(generics.ListCreateAPIView):

#     def post(self, request, *args, **kwargs):
        
        
        


#         return Response('hi')
    

    