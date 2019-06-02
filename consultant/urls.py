from consultant.views import ProductViewSet, ProductCategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'categories', ProductCategoryViewSet, base_name='category')

urlpatterns = router.urls