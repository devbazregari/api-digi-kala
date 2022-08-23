from http.client import HTTPException
from rest_framework import status
from rest_framework.decorators import permission_classes , api_view

from User.models import NewUser
from .serializers import RegisterUserSerializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .utils import hash, verify_password


@api_view(['POST',])
def register(request):


    if request.method == 'POST':

        serializer = RegisterUserSerializers(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()
   
        

        _,token = AuthToken.objects.create(user)

        return Response({

            'mobile':user.mobile,
            'token':token,


        })




@api_view(['POST',])
def login(request):

    if request.method == 'POST':

        try:
            user = NewUser.objects.get(mobile=request.data['mobile'])

        except NewUser.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
        
        if verify_password(request.data['password'],user.password) == False:
            return Response(status.HTTP_400_BAD_REQUEST)
        
        
        _,token = AuthToken.objects.create(user)

        return Response({

            'mobile':user.mobile,
            'token':token,


            })
       
     