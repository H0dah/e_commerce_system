from products.models import Product
from products.serializers import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class ProductList(APIView):
    """
    List all products, or create a new product.
    """
    # get products
    def get(self, request, format='json'):

        sellerUsername = request.query_params.get('seller')

        priceOrder = request.query_params.get('order')

        # make defult order value to be ordered randomly
        option = '?'

        if priceOrder == 'DESC':
            option = '-price'
        elif priceOrder == 'ASC':
            option = 'price'

        if sellerUsername:
            sellerID = User.objects.get(username=sellerUsername).pk
            products = Product.objects.filter(seller= sellerID).order_by(option)
        else:
            products = Product.objects.order_by(option)


        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # create product view
    def post(self, request, format='json'):
        request.data['seller'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)