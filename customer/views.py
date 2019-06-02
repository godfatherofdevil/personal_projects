from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from customer.serializers import ProductSerializer, ProductCategorySerializer
from customer.models import Product, ProductCategory

class UsersProductViewSet(
        mixins.ListModelMixin, 
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    """
    A viewset to list and retrieve products: 
    Allowed access for third party users(customer, supplier)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]

class UsersProductCategoryViewset(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
        """
        A viewset to list and retrieve product categories:
        Allowed access for third party users(customer, supplier)
        """
        queryset = ProductCategory.objects.all()
        serializer_class = ProductCategorySerializer
        permission_classes = [IsAuthenticated,]

