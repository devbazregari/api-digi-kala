from http.client import HTTPException
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import RegisterUserSerializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.authtoken.models import Token



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

        serializer = AuthTokenSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        _,token = AuthToken.objects.create(user)

        return Response({

            'username':user.username,
            'email':user.email,
            'token':token
        })




# @api_view(['POST',])
# def login(request):

#     if request.method == 'POST':

#         try:
#             user = NewUser.objects.get(mobile=request.data['mobile'])

#         except NewUser.DoesNotExist:
#             return Response(status.HTTP_404_NOT_FOUND)
        
        
#         if verify_password(request.data['password'],user.password) == False:
#             return Response(status.HTTP_400_BAD_REQUEST)

        
  
#         token, created = Token.objects.get_or_create(user=user)
        


#         return Response({

#             'mobile':user.mobile,
#             'token':token.key,


#             })
       
     