from django.contrib import admin
from .models import Vendor, Unit, Product, Purchase, Sale, Inventory, Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_mobile']
    search_fields = ['customer_name', 'customer_mobile']
admin.site.register(Customer, CustomerAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'mobile']
    search_fields = ['full_name', 'mobile']
admin.site.register(Vendor, VendorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'unit']
    search_fields = ['title', 'unit']
admin.site.register(Product, ProductAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_name']
    search_fields = ['title', 'short_name']
admin.site.register(Unit, UnitAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'qty', 'price', 'total_amt', 'vendor', 'pur_date']
    search_fields = ['product__title', 'qty', 'vendor']
admin.site.register(Purchase, PurchaseAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'qty', 'price', 'total_amt', 'sale_date']
    search_fields = ['product__title', 'customer', 'qty']
admin.site.register(Sale, SaleAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'pur_qty', 'sale_qty', 'total_bal_qty', 'pur_date', 'sale_date']
    search_fields = ['id', 'product__title']
admin.site.register(Inventory, InventoryAdmin)