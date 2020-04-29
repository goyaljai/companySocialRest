from restapi.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subcategory',SubCategoryViewSet,basename='subcategory')
router.register('maincategory',MainCategoryViewSet)
router.register('app',AppViewSet)

for item in router.urls:
    print(str(item)+"\n")