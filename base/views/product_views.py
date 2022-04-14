from math import prod
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from base.models import *
from base.serializers import *
from rest_framework.permissions import IsAdminUser 





@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request,pk):
   product=Product.objects.get(_id=pk)
   serializer=ProductSerializer(product,many=False)
   return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
   user=request.user
   product=Product.objects.create(
      user=user,
      name='Sample Name',
      price=0,
      brand='Sample brand',
      countInStock=0,
      category='Sample category',
      description=''
   )
   serializer=ProductSerializer(product,many=False)
   return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request,pk):
   data=request.data
   product=Product.objects.get(_id=pk)
   product.name=data['name']
   product.price=data['price']
   product.brand=data['name']
   product.countInStock=data['countInStock']
   product.category=data['category']
   product.description=data['description']

   product.save()

   serializer=ProductSerializer(product,many=False)
   return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request,pk):
   product=Product.objects.get(_id=pk)
   product.delete()
   return Response('Product deleted')
