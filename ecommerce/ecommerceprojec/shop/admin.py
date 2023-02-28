from django.contrib import admin
from . models import Category,Product


class categoryadmin(admin.ModelAdmin):
    list_display=['name','slug','description']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,categoryadmin)

class categoryproduct(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,categoryproduct)