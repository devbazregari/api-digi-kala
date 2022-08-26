from django.db import models
from User.models import User


class Category(models.Model):
    category_id     =   models.BigAutoField(null=False , blank=False , primary_key=True)
    
    name            =   models.CharField( max_length=200, null=False , blank=False , unique=True)


class Attr(models.Model):
    name            =      models.CharField(max_length=2000 , null=False , blank=False)


class Product(models.Model):
    product_id      =      models.BigAutoField(null=False , blank=False , primary_key=True)
    category_id_fk  =      models.ForeignKey(to=Category  , null=False , on_delete=models.CASCADE)
    attrs           =      models.ManyToManyField(to=Attr)       

    cart            =      models.ManyToManyField(to=User)
    title           =      models.CharField(null=False , blank=False , max_length=100)
    brand           =      models.CharField(max_length=100 , null=False , blank=False)
    price           =      models.BigIntegerField(null=False , blank=False)
    mainImage       =      models.CharField(null=False , blank=False , max_length=300)
    brandCategory   =      models.CharField(null=False , blank=False , max_length=200)
    intro           =      models.CharField(null=False , blank=False , max_length=1000)
    overView        =      models.CharField(null=False , blank=False , max_length=1000)
                                                                                # attrs           =      models.JSONField(blank=True, null=True, max_length=10000)





class Sold(models.Model):

    product_id_fk   = models.ForeignKey(to=Product , on_delete=models.CASCADE)
    count           = models.BigIntegerField(blank=True , null=True ,default=0)


    def set_count(self):
        self.count += 1


class Seen(models.Model):

    product_id_fk   =    models.ForeignKey(to=Product , on_delete=models.CASCADE)
    seen            =    models.BigIntegerField(blank=True , null=True ,default=0)

    def set_seen(self):
        self.seen += 1
