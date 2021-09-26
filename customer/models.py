from bakery_admin.models import BakeryItem
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    order_no = models.CharField(max_length=255, blank=True)
    total_price = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=225, blank=True)
    billing_address = models.CharField(max_length=225, blank=True)
    active = BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="order_cr_d", on_delete=CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="order_up_d", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.order_no


class OrderItemMap(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE, null=True, blank=True)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=CASCADE, null=True, blank=True)
    qty = models.IntegerField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    active = BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="order_item_cr_d", on_delete=CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="order_item_up_d", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return "-".join([self.order.order_no, self.bakery_item.name])

