from rest_framework import generics
from .serializers import SnackSerializer
from snacks.models import Snack


class SnackListAPIView(generics.ListAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackCreateAPIView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailAPIView(generics.RetrieveAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
