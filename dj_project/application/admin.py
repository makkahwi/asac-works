from django.contrib import admin
from .models import Item


class AdminItem(admin.ModelAdmin):
    list_display = ["title", "author", "desc", "timestamp", "updated"]


admin.site.register(Item, AdminItem)
