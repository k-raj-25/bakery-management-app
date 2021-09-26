from django.urls import path
from rest_framework.routers import DefaultRouter
from customer.api.views import *

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    # bakery item
    path('bakery-item/list/', BakeryItemListAPIView.as_view()),

    # order
    path('order/create/', OrderCreateAPIView.as_view()),
    path('order/retrieve/<int:pk>/', OrderRetrieveAPIView.as_view()),

]