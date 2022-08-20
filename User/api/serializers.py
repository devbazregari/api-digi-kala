from rest_framework import serializers
from User.models import NewUser
from rest_framework.validators import UniqueValidator

class RegisterUserSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(required = True , validators = [UniqueValidator(NewUser.objects.all())])
    password2 = serializers.CharField(write_only=True , required = True)

    class Meta:
        model = NewUser
        fields = ['email','mobile','password','password2','name','family']


    def validate(self, attrs):
        
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("can't validate data")

        return attrs

    def create(self, validated_data):
        
        user = NewUser(
            mobile = validated_data['mobile'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

