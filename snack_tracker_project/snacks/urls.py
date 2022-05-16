from django.urls import path
from .views import SnackListView, SnacksDetailView

urlpatterns = [
    path("", SnackListView.as_view(), name="List"),
    path("detail/<int:pk>", SnacksDetailView.as_view(), name="Details"),
]
