from rest_framework import serializers
from snacks.models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "purchaser",
            "desc",
            "calories",
            "vegan",
            "gloten_free",
            "sugar_free",
            "lactose_free",
            "timestamp",
            "updated",
        )
        model = Snack
