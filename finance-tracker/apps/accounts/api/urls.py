from django.urls import path

from .views import RegisterAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [

    path(
        "register/",
        RegisterAPIView.as_view(),
        name="api-register"
    ),

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="api-login"
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="api-refresh"
    ),

]