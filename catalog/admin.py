from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'datetime_created', 'datetime_updated')
    
    # list_display_links = ('name', 'sku')
    list_filter = ('is_active',)
    search_fields = ('name',)
