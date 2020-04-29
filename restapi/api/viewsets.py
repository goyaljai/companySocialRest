from restapi.models import *

from .serializers import SubCategorySerializer
from rest_framework import viewsets


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
