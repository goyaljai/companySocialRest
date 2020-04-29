from restapi.api.viewsets import SubCategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subcategory',SubCategoryViewSet)