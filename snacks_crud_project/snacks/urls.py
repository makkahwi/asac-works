from django.urls import path

from .views import (AboutView, SnackCreateView, SnackDeleteView, SnackListView,
                    SnacksDetailView, SnackUpdateView)

urlpatterns = [
    path("", SnackListView.as_view(), name="List"),
    path("snacks/create", SnackCreateView.as_view(), name="Create"),
    path("snacks/<int:pk>", SnacksDetailView.as_view(), name="Snack"),
    path("update/<int:pk>", SnackUpdateView.as_view(), name="Update"),
    path("delete/<int:pk>", SnackDeleteView.as_view(), name="Delete"),
    path("about", AboutView.as_view(), name="About"),
]
