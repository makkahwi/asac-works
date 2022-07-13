from django.urls import path, re_path
from django.views.generic.base import RedirectView
from rest_framework_simplejwt import views as jwt_views

from application.api.viewset import (
    ItemListAPIView,
    ItemDetailAPIView,
    ItemCreateAPIView,
    ItemUpdateAPIView,
    ItemDestroyAPIView,
)

urlpatterns = [
    path("token/obtain", jwt_views.TokenObtainPairView.as_view(), name="JWT Obtain"),
    path("token/refresh", jwt_views.TokenRefreshView.as_view(), name="JWT Refresh"),
    path("api/v1/items", ItemListAPIView.as_view(), name="Item API List"),
    path("api/v1/items/create", ItemCreateAPIView.as_view(), name="Item API Create"),
    path("api/v1/items/<int:pk>", ItemDetailAPIView.as_view(), name="Item API Item"),
    path(
        "api/v1/items/<int:pk>/update",
        ItemUpdateAPIView.as_view(),
        name="Item API Update",
    ),
    path(
        "api/v1/items/<int:pk>/delete",
        ItemDestroyAPIView.as_view(),
        name="Item API Delete",
    ),
    re_path(
        r"^.*$",
        RedirectView.as_view(url="api/v1/items", permanent=False),
        name="Redirect",
    ),
]
