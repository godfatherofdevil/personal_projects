from customer.views import UsersProductViewSet, UsersProductCategoryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', UsersProductViewSet, base_name="user-products")
router.register(r'categories', UsersProductCategoryViewset, base_name="user-categories")

urlpatterns = router.urls