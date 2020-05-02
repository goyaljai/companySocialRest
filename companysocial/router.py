from restapi.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainsubcategory',MainSubCategoryViewSet,basename='mainsubcategory')
router.register('maincategory',MainCategoryViewSet)
router.register('app',AppViewSet)