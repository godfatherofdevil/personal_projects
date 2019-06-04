from django.contrib.auth.models import User
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from shippinguser.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer. The associated view is restricted to only admin users
    """
    country = CountryField()
    class Meta:
        model = CustomUser
        fields = ('email','user_type', 'country', 'phone', 'organization')

class UserCreateSerializer(serializers.ModelSerializer):
    """
    User create serializer to create a new user in our system. 
    The associated view is restricted to only admin users.
    """
    country = CountryField()
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_active', 'user_type', 'country', 'phone', 'organization')
        write_only_fields = ('password',)
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class OrdinaryUserSerializer(serializers.ModelSerializer):
    """
    This serializer is for ordinary users of the system (customer, supplier, consultant)
    They can see their account's details and make modification in allowed fields
    """
    country = CountryField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_active', 'user_type', 'country', 'phone', 'organization')
        write_only_fields = ('password',)
        read_only_fields = ('email', 'is_active', 'user_type')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
