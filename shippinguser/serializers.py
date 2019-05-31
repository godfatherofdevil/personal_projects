from django.contrib.auth.models import User
from rest_framework import serializers
from shippinguser.models import ShippingUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ShippingUserSerializer(serializers.ModelSerializer):
    """
    A shipping user serializer to return the details of users of our shipping application
    """
    user = UserSerializer(required=True)

    class Meta:
        model = ShippingUser
        fields = ('user', 'user_type', 'country', 'phone', 'organization', 'status')
        depth = 1

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of shipping user
        :return: returns a successfully created shipping user record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        shipping_user, created = ShippingUser.objects.update_or_create(user=user,
                            user_type=validated_data.pop('user_type'),
                            country=validated_data.pop('country'),
                            phone=validated_data.pop('phone'),
                            organization=validated_data.pop('organization'),
                            status=validated_data.pop('status'))
        return shipping_user

