from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Item(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Item", kwargs={"pk": self.pk})
