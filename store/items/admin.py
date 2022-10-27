from django.contrib import admin

# Register your models here.

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','slug','date')
    list_filter=('name', 'date','price')
    prepopulated_fields = {'slug' : ('name',)}



admin.site.register(Product, ProductAdmin)

