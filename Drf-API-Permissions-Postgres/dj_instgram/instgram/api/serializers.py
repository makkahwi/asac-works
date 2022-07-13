from rest_framework import serializers
from instgram.models import Photo, Comment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "link",
            "timestamp",
            "updated",
        )
        model = Photo


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "content",
            "post",
            "timestamp",
            "updated",
        )
        model = Comment
