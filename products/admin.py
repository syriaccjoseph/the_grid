from django.contrib import admin

from .models import Product, SubCategory, Category

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
