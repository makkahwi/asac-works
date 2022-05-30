from rest_framework import serializers
from application.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "link",
            "timestamp",
            "updated",
        )
        model = Item
