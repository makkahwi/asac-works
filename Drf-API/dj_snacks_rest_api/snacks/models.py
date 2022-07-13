from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    desc = models.TextField()
    calories = models.IntegerField()
    vegan = models.BooleanField(default=False)
    gloten_free = models.BooleanField(default=False)
    sugar_free = models.BooleanField(default=False)
    lactose_free = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Snack", kwargs={"pk": self.pk})
