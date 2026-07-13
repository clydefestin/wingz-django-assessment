
from django.contrib import admin

from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include("rides.urls")),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
]