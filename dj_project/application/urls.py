from django.urls import path, re_path
from django.views.generic.base import RedirectView

from application.api.viewset import (
    ItemListAPIView,
    ItemDetailAPIView,
    ItemCreateAPIView,
    ItemUpdateAPIView,
    ItemDestroyAPIView,
)

urlpatterns = [
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
]
