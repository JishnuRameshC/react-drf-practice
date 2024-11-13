from rest_framework import routers
from .views import CategoryViewSet, SubcategoryViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubcategoryViewSet)

urlpatterns = router.urls