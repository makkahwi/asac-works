# Lesson 29 Reading

Navigation | [Past Reading](../Read-28/README.md) | [Home Page](../README.md) | [Next Reading](../Read-30/README.md) |

## Django Custom User Model

[Source](https://learndjango.com/tutorials/django-custom-user-model)

Django allows to build customized users model to replace the default pre-bulit one. Steps to do it are as follows...

- Updateing project/settings.py to add the following line...
    AUTH_USER_MODEL = "accounts.CustomUser"
- Creating a Custom User model
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class CustomUser(AbstractUser):
        pass

        def __str__(self):
            return self.username
- Creating new UserCreation and UserChangeForm
    from django import forms
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from .models import CustomUser

    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")
- Update the admin panel
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from .forms import CustomUserCreationForm, CustomUserChangeForm
    from .models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ["email", "username",]

    admin.site.register(CustomUser, CustomUserAdmin)

---

## DjangoX

[Source](https://github.com/wsvincent/djangox)

Text
