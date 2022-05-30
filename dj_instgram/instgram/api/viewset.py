from rest_framework import generics
from .serializers import PhotoSerializer, CommentSerializer
from instgram.models import Photo, Comment
from .permissions import IsOwnerOrReadOnly


class PhotoListAPIView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoCreateAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetailAPIView(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PhotoDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
