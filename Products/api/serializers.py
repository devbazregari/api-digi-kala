from xml.dom import ValidationErr
from rest_framework import serializers
from Products.models import Product , Seen, Sold
import datetime
from User.models import User
from datetime import datetime
from datetime import timedelta

from django.db.models import Max



INCREASE_TIME = 0

class ProductSerializer(serializers.ModelSerializer):

    seen = serializers.SerializerMethodField('get_product_seen')
    attrs = serializers.SerializerMethodField('get_product_attrs')
    # expensive = serializers.SerializerMethodField('get_most_expensive_prod')

    class Meta:
        model = Product
        fields = ['product_id','category_id_fk','title','brand','price','mainImage','brandCategory','intro','overView','seen','attrs']




    # def get_most_expensive_prod(self,product):
        
    #     if 'param' not in self.context:
    #         return None
        

    #     result = Sold.objects.values_list('sold',flat=True).annotate(dcount=Count('sold')).order_by('-dcount')
    
    #     print(result)

    #     return 's'







    def get_product_seen(self,product):

        prod_seen = None
        user  = User.objects.get(pk=self.context["user_id"])

        prod_seen = Seen.objects.get_or_create(prod_id_fk=product , user_id_fk = user) # GET PRODUCT FOR EACH USER
        latest_seen_obj = Seen.objects.filter(prod_id_fk = product.pk).aggregate(Max('seen')) # GET LATEST SEEN
        
        

        permission_time = prod_seen[0].created_on
        time_now = datetime.now()
        ls = latest_seen_obj['seen__max']


        
        if permission_time < time_now:  # MAKING RESTRICTING TIME ( SEEING PRODUCT )
            
            try:
                prev_seen_prod = Seen.objects.filter(prod_id_fk = product.pk).latest('seen')
                prev_seen_prod.last = 'False'
                prev_seen_prod.save() 
              
            except Seen.DoesNotExist as error:
                prev_seen_prod = Seen.objects.filter(prod_id_fk = product.pk).latest('seen')
                
            if prod_seen[1] == True:
                latest_seen = ls+1
                prod_seen[0].seen = latest_seen
                prod_seen[0].last = 'True'

            else:
                prod_seen[0].seen = ls+1
                prod_seen[0].last = 'True'
            
            time_seen = time_now +timedelta(minutes=INCREASE_TIME)
            prod_seen[0].created_on = time_seen
            prod_seen[0].save()      
            

            return prod_seen[0].seen

        else:
            return ls
    

    def get_product_attrs(self,obj):
        attrs = obj.attrs.all()
        return attrs[0].name





