from rest_framework import status
from rest_framework.decorators import permission_classes , api_view
from .serializers import RegisterUserSerializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken



@api_view(['POST',])
def register(request):

    if request.method == 'POST':

        serializer = RegisterUserSerializers(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        _,token = AuthToken.objects.create(user)

        return Response({

            'mobile':user.mobile,
            'email':user.email,
            'toke':token,


        })
