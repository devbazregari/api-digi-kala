from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from Products.models import  Attr, Product , Category 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from User.models import User


@api_view(['POST',])
# @permission_classes((IsAuthenticated,))
def create(request):




    if request.method == 'POST':

        prod_category = Category.objects.get_or_create(name=request.data[0]['category'])
        request.data[0].pop('category')


        product = Product(**request.data[0] , category_id_fk = prod_category[0])
        attr = Attr(**request.data[1])

        attr.save()
        product.save()

        product.attrs.add(attr)

    
        return Response("product saved ")




@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def test(request , pk):


    if request.method == 'GET':
      
        
        return Response('ok')