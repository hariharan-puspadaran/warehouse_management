from django.contrib import admin
from .models import Product, inbound_order, outbound_order
from django.contrib.auth.models import Group

admin.site.site_header = "Warehouse Management Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","quantity")
    list_filter =("category",)
    
class InboundAdmin(admin.ModelAdmin):
    list_display = ("reference","date","sku","quantity","location","remarks")
    list_filter =("date",)

class OutboundAdmin(admin.ModelAdmin):
    list_display = ("reference","date","sku","quantity","destination","remarks")
    list_filter =("date",)
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(inbound_order, InboundAdmin)
admin.site.register(outbound_order, OutboundAdmin)
