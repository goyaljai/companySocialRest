from rest_framework import serializers
from restapi.models import *

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['imagesUrl', 'imagesTitle', 'imagesDescription']