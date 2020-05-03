from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *


class MainSubCategoryViewSet(viewsets.ViewSet):
    queryset = MainSubCategory.objects.all()

    # serializer_class = SubCategorySerializer
    # @action(detail=True, methods=['get'])
    def list(self, request):

        try:
            main_category = MainCategory.objects.get(id=self.request.query_params.get('maincategory_id', None))
            main_sub_categories = MainSubCategory.objects.filter(mainSubCategory=main_category)
        except MainCategory.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            main_sub_categories = MainSubCategory.objects.all()

        print("===========================================================")
        serializer = MainSubCategorySerializer(main_sub_categories, many=True)
        return Response(serializer.data)


class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class OrderRequestsViewSet(viewsets.ModelViewSet):
    queryset = OrderRequests.objects.all()
    serializer_class = OrderRequestsSerializer
