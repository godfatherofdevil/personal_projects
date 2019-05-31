from django.shortcuts import render

from rest_framework import viewsets
from customer.serializers import ProductSerializer, ProductCategorySerializer
from customer.models import Product, ProductCategory

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating and retreiving products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating and retrieving product categories
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
