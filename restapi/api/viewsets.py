from restapi.models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response

class SubCategoryViewSet(viewsets.ViewSet):
    queryset = SubCategory.objects.all()
    #serializer_class = SubCategorySerializer
    #@action(detail=True, methods=['get'])
    def list(self,request):
        try:
            main_category = MainCategory.objects.get(id=self.request.query_params.get('maincategory_id', None))
            sub_categories = SubCategory.objects.filter(mainCategory=main_category)
        except MainCategory.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            sub_categories = SubCategory.objects.all()

        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)


class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer