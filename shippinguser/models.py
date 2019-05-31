from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class ShippingUser(models.Model):
    USER_TYPES = (
        ('customer', 'customer'),
        ('consultant', 'consultant'),
        ('supplier', 'supplier'),
        ('superuser', 'superuser'),
    )

    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer', blank=False)
    country = CountryField(blank_label='(select country)')
    phone = PhoneNumberField(blank=True, default='')
    organization = models.CharField(max_length=100, default='',blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive', blank=False)

    # def create_profile(sender, **kwargs):
    #     user = kwargs["instance"]
    #     if kwargs["created"]:
    #         user_profile = ShippingUser(user=user)
    #         user_profile.save()
    # post_save.connect(create_profile, sender=User)
    

