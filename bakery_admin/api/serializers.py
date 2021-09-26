from django.conf import settings
from rest_framework import serializers
from bakery_admin.models import *
from django.shortcuts import get_object_or_404
import functools


class IngredientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            'name',
            'desc',
            'qty',
            'unit',
            'per_unit_in_kg',
            'cost',
            'sku'
        ]
    
    def create(self, validated_data):
        request = self.context['request']
        ingredient = Ingredient.objects.create(
            **validated_data,
            created_by = request.user,
            updated_by = request.user
        )

        return ingredient
    
    def update(self, instance, validated_data):
        request = self.context['request']

        instance.name = validated_data.get("name", instance.name)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.qty = validated_data.get("qty", instance.qty)
        instance.unit = validated_data.get("unit", instance.unit)
        instance.per_unit_in_kg = validated_data.get("per_unit_in_kg", instance.per_unit_in_kg)
        instance.cost = validated_data.get("cost", instance.cost)
        instance.sku = validated_data.get("sku", instance.sku)
        instance.updated_by = request.user

        instance.save()
        return instance


class IngredientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            'name',
            'desc',
            'qty',
            'unit',
            'per_unit_in_kg',
            'cost',
            'sku'
        ]


class BakeryItemCreateSerializer(serializers.ModelSerializer):
    ingredient_list = serializers.SerializerMethodField()

    class Meta:
        model = BakeryItem
        fields = [
            'name',
            'desc',
            'qty',
            'unit',
            'sell_price',
            'sku',
            'ingredient_list'
        ]
    
    def create(self, validated_data):
        request = self.context['request']
        ingredient_list = request.data['ingredient_list']
        updated_qty = list()
        cost_price = 0

        # validation if we have enough qty of all the ingredients
        # and calculate cost price for bakery item
        for ingredient in ingredient_list:
            ingredient_obj = get_object_or_404(Ingredient, pk=ingredient["ing"])
            ing_total_kg = ingredient_obj.qty * ingredient_obj.per_unit_in_kg
            if ing_total_kg < ingredient["total_kg"] * validated_data["qty"]:
                return False
            per_kg_price = (1/ingredient_obj.per_unit_in_kg) * ingredient_obj.cost
            cost_price += per_kg_price * ingredient["total_kg"]
            ing_total_kg -= ingredient["total_kg"]*validated_data["qty"]
            updated_qty.append({
                **ingredient,
                "qty": int(ing_total_kg/ingredient_obj.per_unit_in_kg)
            })

        bakery_item = BakeryItem.objects.create(
            **validated_data,
            cost_price = cost_price,
            created_by = request.user,
            updated_by = request.user
        )
            
        for ingredient in updated_qty:
            ingredient_obj = get_object_or_404(Ingredient, pk=ingredient["ing"])
            ingredient_obj.qty = ingredient["qty"]
            ingredient_obj.save()
            IngItemMap.objects.create(
                bakery_item = bakery_item,
                ing = ingredient_obj,
                total_kg = ingredient["total_kg"],
                created_by = request.user,
                updated_by = request.user
            )
        
        return bakery_item


class BakeryItemRetrieveSerializer(serializers.ModelSerializer):
    ingredient_list = serializers.SerializerMethodField()

    class Meta:
        model = BakeryItem
        fields = [
            'id',
            'name',
            'desc',
            'qty',
            'unit',
            'cost_price',
            'sell_price',
            'sku',
            'ingredient_list'
        ]

    def get_ingredient_list(self, obj):
        ingredient_list = list(IngItemMap.objects.filter(bakery_item=obj, active=True).values("ing", "total_kg"))
        total_kg_bakery = functools.reduce(lambda a,b: a["total_kg"]+b["total_kg"], ingredient_list)
        ingredient_list = [{**x, "qty_percent":float("{:.2f}".format(x["total_kg"]*100/total_kg_bakery))} for x in ingredient_list]

        return ingredient_list


class BakeryItemManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakeryItem
        fields = [
            'qty'
        ]

    def update(self, instance, validated_data):
        request = self.context['request']
        ingredient_list = list(IngItemMap.objects.filter(bakery_item=instance).values("ing", "total_kg"))
        updated_qty = list()
        cost_price = 0

        # validation if we have enough qty of all the ingredients
        # and calculate cost price for bakery item
        for ingredient in ingredient_list:
            ingredient_obj = get_object_or_404(Ingredient, pk=ingredient["ing"])
            ing_total_kg = ingredient_obj.qty * ingredient_obj.per_unit_in_kg
            if ing_total_kg < ingredient["total_kg"] * validated_data["qty"]:
                return False
            per_kg_price = (1/ingredient_obj.per_unit_in_kg) * ingredient_obj.cost
            cost_price += per_kg_price * ingredient["total_kg"]
            ing_total_kg -= ingredient["total_kg"]*validated_data["qty"]
            updated_qty.append({
                "ing": ingredient["ing"],
                "qty": int(ing_total_kg/ingredient_obj.per_unit_in_kg)
            })

        instance.qty += validated_data["qty"]
        instance.cost_price = cost_price
        instance.save()

        for ingredient in updated_qty:
            ingredient_obj = get_object_or_404(Ingredient, pk=ingredient["ing"])
            ingredient_obj.qty = ingredient["qty"]
            ingredient_obj.save()
        
        return instance