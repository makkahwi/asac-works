from django.contrib import admin
from .models import Photo, Comment


class AdminPhoto(admin.ModelAdmin):
    list_display = ["title", "author", "link", "timestamp", "updated"]


admin.site.register(Photo, AdminPhoto)


class AdminComment(admin.ModelAdmin):
    list_display = ["author", "content", "post", "timestamp", "updated"]


admin.site.register(Comment, AdminComment)
