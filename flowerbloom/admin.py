# Register your models here.

from django.contrib import admin
from django.utils.html import format_html
from . models import Flower
from . models import Product, Category

# Register your models here.
@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display=('admin_id','admin_name')

admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def prdImg(self,obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    list_display=('name','description','price','prdImg','category','product_info','delivery_charge','delivery_info')
