from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Snack(models.Model):
    name = models.CharField(max_length=64)
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

    def __str__(self):
        return self.name
