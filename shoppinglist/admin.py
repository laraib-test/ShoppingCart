from django.contrib import admin
from .models import Category, Product, Store, Price
# Register your models here.
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Price)
admin.site.register(Category)
