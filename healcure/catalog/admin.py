from django.contrib import admin
from .models import Product, Category

# Register your models here.


#Admin registration class with decorator
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'brand', 'main_desc','category', 'price')
    list_filter = ('name','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

