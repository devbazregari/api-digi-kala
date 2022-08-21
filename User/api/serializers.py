from rest_framework import serializers
from User.models import NewUser
from rest_framework.validators import UniqueValidator
from .utils import hash

class RegisterUserSerializers(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True , required = True)

    class Meta:
        model = NewUser
        fields = ['mobile','password','password2']


    def validate(self, attrs):
        
        print(attrs)
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("can't validate data")

        return attrs

    def create(self, validated_data):
        
        hash_pass = hash(validated_data['password'])
        user = NewUser(
            mobile = validated_data['mobile'],
        )

        user.password = hash_pass
        user.save()
        return user

