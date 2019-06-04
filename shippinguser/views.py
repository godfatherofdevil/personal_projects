from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from shippinguser.serializers import UserSerializer, UserCreateSerializer, OrdinaryUserSerializer
from shippinguser.models import CustomUser
from shippinguser.permissions import IsCurrentUser

class SuperUserViewSet(viewsets.ModelViewSet):
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
    create_serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser,]

    def get_serializer_class(self):
        if self.action == 'create':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class
        return super(SuperUserViewSet, self).get_serializer_class()

class OrdinaryUserViewset(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet
        ):
    
    serializer_class = OrdinaryUserSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]

    def get_queryset(self):
        """
        filter the queryset based on current logged in user
        """
        user = self.request.user

        return CustomUser.objects.filter(email=user.email)
