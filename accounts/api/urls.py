from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.api.views import (
    LoginAPIView, LogoutAPIView, RegisterAPIView
)


router = DefaultRouter()
urlpatterns = router.urls

urlpatterns.append(path('login/', LoginAPIView.as_view()))
urlpatterns.append(path('logout/', LogoutAPIView.as_view()))
urlpatterns.append(path('register/', RegisterAPIView.as_view()))
