from django.urls import path, re_path
from django.views.generic.base import RedirectView

from instgram.api.viewset import (
    PhotoListAPIView,
    PhotoDetailAPIView,
    PhotoCreateAPIView,
    PhotoUpdateAPIView,
    PhotoDestroyAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDestroyAPIView,
)

urlpatterns = [
    path("api/v1/photos", PhotoListAPIView.as_view(), name="Photo API List"),
    path("api/v1/photos/create", PhotoCreateAPIView.as_view(), name="Photo API Create"),
    path(
        "api/v1/photos/<int:pk>", PhotoDetailAPIView.as_view(), name="Photo API Photo"
    ),
    path(
        "api/v1/photos/<int:pk>/update",
        PhotoUpdateAPIView.as_view(),
        name="Photo API Update",
    ),
    path(
        "api/v1/photos/<int:pk>/delete",
        PhotoDestroyAPIView.as_view(),
        name="Photo API Delete",
    ),
    path("api/v1/comments", CommentListAPIView.as_view(), name="Comment API List"),
    path(
        "api/v1/comments/create",
        CommentCreateAPIView.as_view(),
        name="Comment API Create",
    ),
    path(
        "api/v1/comments/<int:pk>",
        CommentDetailAPIView.as_view(),
        name="Comment API Comment",
    ),
    path(
        "api/v1/comments/<int:pk>/update",
        CommentUpdateAPIView.as_view(),
        name="Comment API Update",
    ),
    path(
        "api/v1/comments/<int:pk>/delete",
        CommentDestroyAPIView.as_view(),
        name="Comment API Delete",
    ),
    re_path(
        r"^.*$",
        RedirectView.as_view(url="api/v1/photos", permanent=False),
        name="Landing",
    ),
]
