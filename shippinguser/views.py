from django.shortcuts import render
from rest_framework import viewsets
from shippinguser.serializers import ShippingUserSerializer
from shippinguser.models import ShippingUser

class UserViewSet(viewsets.ModelViewSet):
    """"
    viewset to create and retrieve users in our shipping application
    """
    queryset = ShippingUser.objects.all()
    serializer_class = ShippingUserSerializer
