# from xml.dom.expatbuilder import theDOMImplementation
# from django.shortcuts import render
from django.http import JsonResponse
from .models import MarketCategory,Player,Product
from .serializers import MarketCategorySerializer,PlayerSerializer,ProductSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def market_list(request,format=None):
    if request.method =='GET':
        # get all the Market categories
        markets = MarketCategory.objects.all()
        # serialize them
        serializer = MarketCategorySerializer(markets, many=True)
        # return json
        return JsonResponse(serializer.data,safe=False)
    if request.method =='POST':
        serializer = MarketCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def market_details(request,id,format=None):
    """Getting,updating and deleting item from market using id"""
    
    try:
       market = MarketCategory.objects.get(pk=id)
    except MarketCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = MarketCategorySerializer(market)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=='PUT':
        serializer = MarketCategorySerializer(market,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def player_list(request):
    # get all the Market categories
    players = Player.objects.all()
    # serialize them
    serializer = PlayerSerializer(players, many=True)
    # return json
    return JsonResponse(serializer.data)


def product_list(request):
    # get all the Market categories
    products = Product.objects.all()
    # serialize them
    serializer = ProductSerializer(products, many=True)
    # return json
    return JsonResponse(serializer.data,safe=False)