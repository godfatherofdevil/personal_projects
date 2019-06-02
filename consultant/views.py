from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from customer.models import Product, ProductCategory
from customer.serializers import ProductSerializer, ProductCategorySerializer
from shippinguser.permissions import IsConsultant, IsSuperUser

class ProductViewSet(mixins.ListModelMixin, 
        mixins.CreateModelMixin, 
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """
    A viewset for creating and retreiving products
    This can be accessed only by either superuser or consultants ->
    No third party user access is allowed (customer, supplier)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsConsultant|IsSuperUser,]

class ProductCategoryViewSet(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """
    A viewset for creating and retrieving product categories
    This can be accessed only by either superuser or consultants ->
    No third party user access is allowed (customer, supplier)
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsConsultant|IsSuperUser,]
