from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField


INGREDIENTS = (
    ("PCS", "Pieces"),
    ("KG", "Kilogram"),
    ("GM", "Gram"),
    ("Dozen", "Dozen"),
    ("LTR", "Litre")
)

class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    qty = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20, choices=INGREDIENTS, blank=True)
    per_unit_in_kg = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    sku = models.CharField(max_length=25, blank=True)
    active = BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="ing_cr_d", on_delete=CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="ing_up_d", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class BakeryItem(models.Model):
    name = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    qty = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20, choices=INGREDIENTS, blank=True)
    cost_price = models.FloatField(blank=True, null=True)
    sell_price = models.FloatField(blank=True, null=True)
    sku = models.CharField(max_length=25, blank=True)
    active = BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="bak_cr_d", on_delete=CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="bak_up_d", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class IngItemMap(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, on_delete=CASCADE, null=True, blank=True)
    ing = models.ForeignKey(Ingredient, on_delete=CASCADE, null=True, blank=True)
    total_kg = models.FloatField(blank=True, null=True)
    active = BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="ingbak_cr_d", on_delete=CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="ingbak_up_d", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return "-".join([self.bakery_item.name, self.ing.name])

