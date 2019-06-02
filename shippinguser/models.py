from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from shippinguser.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('customer', 'customer'),
        ('consultant', 'consultant'),
        ('supplier', 'supplier'),
        ('superuser', 'superuser'),
    )
    
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer', blank=False)
    country = CountryField(blank_label='(select country)')
    phone = PhoneNumberField(blank=True, default='')
    organization = models.CharField(max_length=100, default='',blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    

