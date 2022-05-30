# Django Authentication & Prodcution Server

LTUC Django-Based Project

## How to recreate

1. Run following CLI commands
    - poetry new [dj-auth]
    - cd [dj-auth]
    - poetry install
    - poetry shell
    - poetry add django djangorestframework
    - django-admin startproject [dj_project]
    - cd [dj_project]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [application]
    - Add [application] to INSTALLED_APPS list in [dj_project]/settings.py

2. Create your models
    - Add models construction in [application]/models.py
    - Register model in [application]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Do REST API configs
    - Add "rest_framework" to INSTALLED_APPS list in [dj_project]/settings.py
    - Add default rest configs in tail of [dj_project]/settings.py
            REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
    - Create [application]/api/serializers.py & link models
    - Create [application]/api/viewset.py & link models & serializers
    - Create urls.py in [application] directory
    - Link created urls.py to [dj_project]/urls.py
    - Add API URLs to [application]/urls.py

## How to start

- python manage.py runserver

## APIs

| -- | -------------------------- | ------------------- |
| #  | Link                       | Function            |
| -- | -------------------------- | ------------------- |
| 01 | api/v1/items              | Items API List     |
| 02 | api/v1/items/create       | Item API Create    |
| 03 | api/v1/items/:id          | Item API Details   |
| 04 | api/v1/items/:id/update   | Item API Update    |
| 05 | api/v1/items/:id/delete   | Item API Delete    |
