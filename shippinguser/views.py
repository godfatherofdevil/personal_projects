from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from shippinguser.serializers import UserSerializer
from shippinguser.models import CustomUser

class UserViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """
    viewset to list, retrieve and update users in our shipping application
    This view is restricted to only admin users, any kind of modification for User Models should be done by admin
    list : GET request will list all the users
    retrieve: GET request with specific 'id' will retrieve that user
    update: PUT request with all mandotary fields (not blank and not null) will update that user with given values.
    To perform partial update on some field - make PATCH request with value for that field
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
