# django
from django.contrib import admin

# custom
from customer.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_no", "user", "total_price", "date"]


@admin.register(OrderItemMap)
class OrderItemMapAdmin(admin.ModelAdmin):
    list_display = ["order", "bakery_item", "qty", "unit_price"]