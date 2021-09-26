from django.urls import path
from rest_framework.routers import DefaultRouter
from bakery_admin.api.views import *

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    # ingredients
    path('ingredient/create/', IngredientCreateAPIView.as_view()),
    path('ingredient/update/<int:pk>/', IngredientUpdateAPIView.as_view()),
    path('ingredient/list/', IngredientListAPIView.as_view()),
    path('ingredient/detail/<int:pk>/', IngredientRetrieveAPIView.as_view()),
    path('ingredient/delete/<int:pk>/', IngredientDestroyAPIView.as_view()),

    # bakery item
    path('bakery-item/create/', BakeryItemCreateAPIView.as_view()),
    path('bakery-item/manage/<int:pk>/', BakeryItemManageAPIView.as_view()),
    path('bakery-item/detail/<int:pk>/', BakeryItemRetrieveAPIView.as_view()),
    
]