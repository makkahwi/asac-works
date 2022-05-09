from django.db import models


class Snack(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    calories = models.IntegerField()
    vegan = models.BooleanField(default=False)
    gloten_free = models.BooleanField(default=False)
    sugar_free = models.BooleanField(default=False)
    lactose_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name
