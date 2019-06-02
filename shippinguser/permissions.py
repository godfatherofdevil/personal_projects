from shippinguser.models import CustomUser
from rest_framework.permissions import BasePermission

class IsConsultant(BasePermission):
    """
    Permission class to determine if the current user is consultant
    """
    def has_permission(self, request, view):
        """
        check if current user's user_type is consultant then return True, otherwise return False
        if not logged in (Anonymous user) then return False
        """
        try:
            if request.user.user_type == "consultant":
                return True
        except Exception as e:
            return False
        return False

class IsCustomerOrSupplier(BasePermission):
    """
    Permission class to determine if the current user is either customer or supplier ->
    (third party users of our application)
    """
    def has_permission(self, request, view):
        """
        Check if current user's user_type is customer or supplier then return True, otherwise return False
        if not logged in (Anonymous user) then return False
        """
        try:
            if (request.user.user_type == "customer") or (request.user.user_type == "supplier"):
                return True
        except Exception as e:
            return False
        return False

class IsSuperUser(BasePermission):
    """
    Permission class to determine if the current user is superuser
    superuser has all access in our application
    """
    def has_permission(self, request, view):
        """
        Check if current user's user_type is superuser then return True, otherwise False
        if not logged in (Anonymous user) then return False
        """
        try:
            if request.user.user_type == "superuser":
                return True
        except Exception as e:
            return False
        return False
