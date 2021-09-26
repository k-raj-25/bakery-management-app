from rest_framework import serializers
from bakery_admin.models import BakeryItem
from customer.models import *
from django.shortcuts import get_object_or_404


class BakeryItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakeryItem
        fields = [
            'name',
            'desc',
            'unit',
            'sell_price'
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    items_list = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'total_price',
            'shipping_address',
            'billing_address',
            'items_list'
        ]

    def create(self, validated_data):
        request = self.context['request']
        items_list = request.data["items_list"]

        # validation if we have enough qty of all the bakery items
        for item in items_list:
            bakery_item_obj = get_object_or_404(BakeryItem, pk=item["bakery_item"])
            if bakery_item_obj.qty < item["qty"]:
                error = {"success":False, "message": "You don't have enough stock!", "data":{}}
                raise serializers.ValidationError(error)
            item["bakery_item_qty"] = bakery_item_obj.qty - item["qty"]

        if Order.objects.all().count():
            order_no = "ORDER{}".format(Order.objects.latest("pk").id + 1)
        else:
            order_no = "ORDER1"

        order = Order.objects.create(
            **validated_data,
            order_no = order_no,
            user = request.user,
            created_by = request.user,
            updated_by = request.user
        )

        for item in items_list:
            bakery_item_obj = get_object_or_404(BakeryItem, pk=item["bakery_item"])
            bakery_item_obj.qty = item["bakery_item_qty"]
            bakery_item_obj.save()
            item["bakery_item"] = bakery_item_obj
            item.pop('bakery_item_qty', None)
            order_item = OrderItemMap.objects.create(
                **item,
                order = order,
                created_by = request.user,
                updated_by = request.user
            )

        return order


class OrderRetrieveSerializer(serializers.ModelSerializer):
    items_list = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'order_no',
            'total_price',
            'date',
            'shipping_address',
            'billing_address',
            'items_list'
        ]

    def get_items_list(self, obj):
        return list(OrderItemMap.objects.filter(order=obj, active=True).values("bakery_item", "qty", "unit_price"))