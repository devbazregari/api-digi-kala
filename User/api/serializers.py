from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from User.models import User
from .utils import hash
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class RegisterUserSerializers(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True , required = True)
    # email = serializers.EmailField(required = True , validators = [UniqueValidator(NewUser.objects.all())])

    class Meta:
        model = User
        fields = ['mobile','password','password2']


    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("can't validate data")

        mobile = attrs['mobile']

        try:
            int(mobile)

        except:
            raise serializers.ValidationError("enter a valid phone number ")

        if mobile[0] != "0" or mobile[1] != "9":
            raise serializers.ValidationError("enter a valid phone number ") 

        return attrs
    def create(self, validated_data):
        
        hash_pass = hash(validated_data['password'])
        user = User(
            mobile = validated_data['mobile']
        )

        user.password = hash_pass
        user.save()
        return user



