from rest_framework import serializers
from application.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "desc",
            "timestamp",
            "updated",
        )
        model = Item
