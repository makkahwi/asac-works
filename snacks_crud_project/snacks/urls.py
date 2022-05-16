from django.urls import path
from .views import SnackListView, SnacksDetailView, AboutView

urlpatterns = [
    path("", SnackListView.as_view(), name="List"),
    path("snack/<int:pk>", SnacksDetailView.as_view(), name="Snack"),
    path("about", AboutView.as_view(), name="About"),
]
