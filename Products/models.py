from time import timezone
from django.db import models
from User.models import User
from datetime import datetime



class Attr(models.Model):
    name = models.CharField(max_length=2000, null=False, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)





class Product(models.Model):
    product_id      =   models.BigAutoField(null=False, blank=False, primary_key=True)
    attrs           =   models.ManyToManyField(to=Attr)
    cart            =   models.ManyToManyField(to=User)
    category_id_fk  =   models.ForeignKey(to=Category , on_delete=models.CASCADE)


    title           =   models.CharField(null=False, blank=False, max_length=100)
    brand           =   models.CharField(max_length=100, null=False, blank=False)
    price           =   models.BigIntegerField(null=False, blank=False)
    mainImage       =   models.CharField(null=False, blank=False, max_length=300)
    brandCategory   =   models.CharField(null=False, blank=False, max_length=200)
    intro           =   models.CharField(null=False, blank=False, max_length=1000)
    overView        =   models.CharField(null=False, blank=False, max_length=1000)
    # attrs           =      models.JSONField(blank=True, null=True, max_length=10000) this could be here 


class Seen(models.Model):
   
    seen            =   models.BigIntegerField(blank=True, null=True, default=0)
    user_id_fk      =   models.ForeignKey(to = User ,blank=False , null= False , on_delete=models.CASCADE)
    prod_id_fk      =   models.ForeignKey(to = Product ,blank=False , null= False , on_delete=models.CASCADE)
    last            =   models.CharField(default='True' , max_length=10)
    created_on      =   models.DateTimeField(default = datetime.now())



class Sold(models.Model):

    sold            =   models.BigIntegerField(blank=True, null=True, default=0)
    user_id_fk      =   models.ForeignKey(to = User ,blank=False , null= False , on_delete=models.CASCADE)
    prod_id_fk      =   models.ForeignKey(to = Product ,blank=False , null= False , on_delete=models.CASCADE)
    #last            =   models.CharField(default='True' , max_length=10)
    created_on      =   models.DateTimeField(default = datetime.now())






