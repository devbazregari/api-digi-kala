from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self,  password, **kwargs):
  

        user = self.model(**kwargs)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self , password, **kwargs):
        user = self.create_user( password, **kwargs)

        user.is_admin = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):

    mobile    = models.CharField(max_length=11 , blank=False , null=False , unique=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    