from rest_framework import status
from rest_framework.decorators import api_view
from User.models import User
from .utils import verify_password
from .serializers import RegisterUserSerializers
from rest_framework.response import Response
from knox.auth import AuthToken



@api_view(['POST',])
def register(request):


    if request.method == 'POST':


        serializer = RegisterUserSerializers(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()



        _,token = AuthToken.objects.create(user)

        return Response({

            'user_id':user.pk,
            'mobile':user.mobile,
            'token':token,


        })







@api_view(['POST',])
def login(request):

    if request.method == 'POST':

        try:
            user = User.objects.get(mobile=request.data['mobile'])

        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


        if verify_password(str(request.data['password']),user.password) == False:
            return Response(status.HTTP_400_BAD_REQUEST)


        _,token = AuthToken.objects.create(user)

        print(token)
        return Response({

            'user_id':user.pk,
            'mobile':user.mobile,
            'token':str(token),


            })

