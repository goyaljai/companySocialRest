from rest_framework import serializers
from restapi.models import *


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','imagesUrl','imagesTitle','imagesDescription']

class MainSubCategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = MainSubCategory
        fields = ['id','description','subcategories']

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id','title']

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id','title','appUrl', 'appTitle', 'appMainImage']
