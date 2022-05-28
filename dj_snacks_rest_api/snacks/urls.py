from django.urls import path

from .views import (
    AboutView,
    SnackCreateView,
    SnackDeleteView,
    SnackListView,
    SnacksDetailView,
    SnackUpdateView,
)

from snacks.api.viewset import (
    SnackListAPIView,
    SnackDetailAPIView,
    SnackCreateAPIView,
    SnackUpdateAPIView,
    SnackDestroyAPIView,
)

urlpatterns = [
    path("", SnackListView.as_view(), name="List"),
    path("snacks/create", SnackCreateView.as_view(), name="Create"),
    path("snacks/<int:pk>", SnacksDetailView.as_view(), name="Snack"),
    path("snacks/<int:pk>/update", SnackUpdateView.as_view(), name="Update"),
    path("snacks/<int:pk>/delete", SnackDeleteView.as_view(), name="Delete"),
    path("about", AboutView.as_view(), name="About"),
    path("api/v1/snacks", SnackListAPIView.as_view(), name="API List"),
    path("api/v1/snacks/create", SnackCreateAPIView.as_view(), name="API Create"),
    path("api/v1/snacks/<int:pk>", SnackDetailAPIView.as_view(), name="API Snack"),
    path(
        "api/v1/snacks/<int:pk>/update",
        SnackUpdateAPIView.as_view(),
        name="API Update",
    ),
    path(
        "api/v1/snacks/<int:pk>/delete",
        SnackDestroyAPIView.as_view(),
        name="API Delete",
    ),
]
