from shippinguser.views import SuperUserViewSet, OrdinaryUserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'super-users', SuperUserViewSet, base_name='super-user')
router.register(r'users', OrdinaryUserViewset, base_name='ordinary-user')

urlpatterns = router.urls