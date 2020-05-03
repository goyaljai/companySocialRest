from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(App)
admin.site.register(MainCategory)
admin.site.register(MainSubCategory)

class OrderRequestsAdmin(admin.ModelAdmin):
    search_fields = ['item_id','name','item_name']

class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['id','imagesDescription']


admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(OrderRequests,OrderRequestsAdmin)