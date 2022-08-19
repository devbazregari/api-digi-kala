from django.db import models
from django.contrib.auth.models import PermissionsMixin , AbstractBaseUser , BaseUserManager

class UserManager(BaseUserManager):

    def create_superuser(self, email , mobile , password , **other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)

        if not email:
            raise ValueError("the user must have an specefic email ")
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(" the superuser's is_staff must be true ")
        

        if other_fields.get('is_active') is not True:
            raise ValueError(" the superuser's is_active must be true ")


        return self.create_user(email = email , mobile = mobile , password = password , **other_fields)


    def create_user(self , email , mobile , password , **other_fields ):
        
        if not email:
            raise ValueError("the user must have an specefic email ")
        
        email = self.normalize_email(email)
        user = self.model(email = email , mobile = mobile , password = password , **other_fields)
        user.set_password(password)
        user.save()

        return user


class NewUser(AbstractBaseUser , PermissionsMixin):
    name   = models.CharField(max_length=60 , null=True , blank=True)
    family = models.CharField(max_length=100 , null=True , blank=True)
    email  = models.EmailField(unique=True , null=False , blank=True)
    mobile = models.BigIntegerField(unique=True , null=False , blank=True)
    #cart  = 
    
    # Admin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']    

    objects = UserManager()
    
    def __str__(self) -> str:
        return self.email