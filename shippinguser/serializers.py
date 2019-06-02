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
