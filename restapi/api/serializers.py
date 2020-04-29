from rest_framework import serializers
from restapi.models import *

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','imagesUrl', 'imagesTitle', 'imagesDescription']

class MainCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id','title','imagesUrl', 'imagesTitle', 'imagesDescription']

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['id','title','imagesUrl', 'imagesTitle', 'imagesDescription']