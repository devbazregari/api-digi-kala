from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.views import AuthTokenSerializer
from User.models import NewUser
from django.contrib.auth import authenticate
from User.models import NewUser



class LoginUserSerializers(serializers.ModelSerializer):

    mobile = serializers.CharField(required=True)
    email = serializers.EmailField(required=True )
    password = serializers .CharField(required=True , write_only=True)

    class Meta:
        model = NewUser
        fields = ['mobile','email','password']


    def validate(self, attrs):
        email = attrs['email']
        mobile = attrs['mobile']
        password = attrs['password']

        try:
            user_query = NewUser.objects.get(mobile=mobile)

        except NewUser.DoesNotExist:
            raise serializers.ValidationError(" there isn't an user with thin credentials")
      
        user = authenticate(username=email,password=password)

        if not user:
            raise serializers.ValidationError(" false credentials ")

        if int(mobile) != user_query.mobile:
            raise serializers.ValidationError("can't validate data  ")

        return {'user_query':user_query}

class UserRegisterSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(required  = True , validators   = [UniqueValidator(NewUser.objects.all())])
    password2 = serializers.CharField(required = True , write_only = True)
    family = serializers.CharField(required = True)
    name = serializers.CharField(required = True)

    class Meta:
        model = NewUser
        fields = ['email','mobile','password','password2','name','family']

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("can't validate data")
    
        return attrs
    
    def create(self,validated_data):

        try:
            user = NewUser( mobile=validated_data['mobile'],email=validated_data['email'],name=validated_data['name'] , family= validated_data['family'])
        
        except NewUser.DoesNotExist:
            raise serializers.ValidationError("false credentials ") 
        
        user.set_password(validated_data['password'])
        user.save()
        return user