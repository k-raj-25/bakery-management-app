from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from customer.api.serializers import *


class BakeryItemListAPIView(generics.ListAPIView):

    def get(self, request):
        queryset = BakeryItem.objects.filter(active=True).order_by('-pk').prefetch_related()
        serializer = BakeryItemListSerializer(queryset, many=True)

        return Response({"success":True, "message":"", "data":serializer.data}, status=status.HTTP_200_OK)


class OrderCreateAPIView(generics.CreateAPIView):

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message": "Order created successfully!", "data":{}}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "message":"", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrderRetrieveAPIView(generics.RetrieveAPIView):

    def get(self, request, pk=None):
        instance = get_object_or_404(Order, pk=pk)
        serializer = OrderRetrieveSerializer(instance)

        return Response({"success":True, "message":"", "data":serializer.data}, status=status.HTTP_200_OK)
