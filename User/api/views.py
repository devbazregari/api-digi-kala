from User.models import NewUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegisterSerializers , LoginUserSerializers
from rest_framework import generics
from knox.auth import AuthToken



class UserLoginListCreateAPIView(generics.ListCreateAPIView):

    def __init__(self):
        self.queryset = NewUser.objects.all()
        self.serializer_class = UserRegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user_query']
        _,token = AuthToken.objects.create(user)

        return Response({

            'mobile':user.mobile,
            'email':user.email,
            'token':token
        })

    def list(self):
        serializer = UserRegisterSerializers(self.queryset, many=True)
        return Response(serializer.data)


class UserRegister(generics.ListCreateAPIView):

    def post(self,request):

        serializer = UserRegisterSerializers(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()


        return Response({

            'name':user.name,
            'email':user.email,
            'mobile':user.mobile
        })
        
        












# @api_view(['POST',])
# def login(request):

#     if request.method == 'POST':

#         serializer = LoginUserSerializers(data=request.data)


#         serializer.is_valid(raise_exception=True)

        
#         user = serializer.validated_data['user_query']

#         _,token = AuthToken.objects.create(user)

#         return Response({

#             'mobile':user.mobile,
#             'email':user.email,
#             'token':token
#         })




   
