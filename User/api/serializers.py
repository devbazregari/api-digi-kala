from rest_framework import serializers
from User.models import NewUser
from rest_framework.validators import UniqueValidator

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
        
        user = NewUser(
            mobile = validated_data['mobile'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

