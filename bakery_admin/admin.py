# django
from django.contrib import admin

# custom
from bakery_admin.models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "qty", "cost", "sku", "active"]


@admin.register(BakeryItem)
class BakeryItemAdmin(admin.ModelAdmin):
    list_display = ["name", "qty", "cost_price", "sell_price", "sku", "active"]


@admin.register(IngItemMap)
class IngItemMapAdmin(admin.ModelAdmin):
    list_display = ["bakery_item", "ing", "active"]