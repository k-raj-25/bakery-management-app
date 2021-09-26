from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from bakery_admin.api.serializers import *


# ingerient create view
class IngredientCreateAPIView(generics.CreateAPIView):

    def post(self, request):
        serializer = IngredientCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message": "Ingredient created successfully!", "data":{}}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "message":"", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class IngredientUpdateAPIView(generics.UpdateAPIView):

    def put(self, request, pk=None):
        instance = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientCreateSerializer(instance, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message": "Ingredient updated successfully!", "data":{}}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "message":"", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class IngredientListAPIView(generics.ListAPIView):

    def get(self, request):
        queryset = Ingredient.objects.filter(active=True).order_by('-pk').prefetch_related()
        serializer = IngredientListSerializer(queryset, many=True)

        return Response({"success":True, "message":"", "data":serializer.data}, status=status.HTTP_200_OK)


class IngredientRetrieveAPIView(generics.RetrieveAPIView):

    def get(self, request, pk=None):
        instance = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientListSerializer(instance)

        return Response({"success":True, "message":"", "data":serializer.data}, status=status.HTTP_200_OK)

    
class IngredientDestroyAPIView(generics.DestroyAPIView):

    def destroy(self, request, pk=None):
        queryset = Ingredient.objects.filter(pk=pk).update(active=False)

        return Response({"success":True, "message":"Ingredient deleted successfully.", "data":{}}, status=status.HTTP_200_OK)


class BakeryItemCreateAPIView(generics.CreateAPIView):

    def post(self, request):
        serializer = BakeryItemCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message": "Bakery Item created successfully!", "data":{}}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "message":"", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BakeryItemRetrieveAPIView(generics.RetrieveAPIView):

    def get(self, request, pk=None):
        queryset = get_object_or_404(BakeryItem, pk=pk)
        serializer = BakeryItemRetrieveSerializer(queryset)

        return Response({"success":True, "message":"", "data":serializer.data}, status=status.HTTP_200_OK)


class BakeryItemManageAPIView(generics.UpdateAPIView):

    def put(self, request, pk=None):
        instance = get_object_or_404(BakeryItem, pk=pk)
        serializer = BakeryItemManageSerializer(instance, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message": "Quantity updated successfully!", "data":{}}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "message":"", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
