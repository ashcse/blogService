from django.shortcuts import render

from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

from .serializers import ProductSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail View': '/product-create/',
        'Create': '/product-create/',
        'Update': '/product-update/',
        'Delete': '/product-delete/',        
    }
    
    return Response(api_urls)


@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save();        
    
    return Response(serializer.data)
    

