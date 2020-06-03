from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

admin.site.register(App)
admin.site.register(MainCategory)
admin.site.register(MainSubCategory)

class OrderRequestsAdmin(admin.ModelAdmin):
    search_fields = ['item_id','name','item_name']

class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['id','imagesDescription']
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.imagesUrl.url))

    image_tag.short_description = 'Image'
    
    def get_name(self,obj):
        return '%s -> %s -> %s' % (obj.mainSubCategory.mainSubCategory.title,obj.mainSubCategory.description,obj.imagesDescription)
        
    get_name.short_description = 'MainCategory -> SubCategory -> Image Description'

    list_display = ['get_name','image_tag',]


admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(OrderRequests,OrderRequestsAdmin)