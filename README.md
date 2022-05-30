# Django Permissions & PostgreSQL DB

LTUC Django-Based Project

## How to recreate

1. Run following CLI commands
    - poetry new [dj-instgram]
    - cd [dj-instgram]
    - poetry install
    - poetry shell
    - poetry add django django-filter djangorestframework Markdown
    - django-admin startproject [dj_instgram]
    - cd [dj_instgram]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [instgram]
    - Add [instgram] to INSTALLED_APPS list in [dj_instgram]/settings.py

2. Create your models
    - Add models construction in [instgram]/models.py
    - Register model in [instgram]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Do REST API configs
    - Add "rest_framework" to INSTALLED_APPS list in [dj_instgram]/settings.py
    - Add default rest configs in tail of [dj_instgram]/settings.py
            REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
    - Create [instgram]/api/serializers.py & link models
    - Create [instgram]/api/viewset.py & link models & serializers
    - Create urls.py in [instgram] directory
    - Link created urls.py to [dj_instgram]/urls.py
    - Add API URLs to [instgram]/urls.py

5. Add Permissions
    - Adjust REST_FRAMEWORK list of [dj_instgram]/settings.py to...
            rest_framework.permissions.IsAuthenticated
    - Create [instgram]/api/permissions.py
    - Link created permissions to views of [instgram]/api/viewset.py

## How to start

- python manage.py runserver

## APIs

| -- | -------------------------- | ------------------- |
| #  | Link                       | Function            |
| -- | -------------------------- | ------------------- |
| 01 | api/v1/photos              | Photos API List     |
| 02 | api/v1/photos/create       | Photo API Create    |
| 03 | api/v1/photos/:id          | Photo API Details   |
| 04 | api/v1/photos/:id/update   | Photo API Update    |
| 05 | api/v1/photos/:id/delete   | Photo API Delete    |
| 06 | api/v1/comments            | Comments API List   |
| 07 | api/v1/comments/create     | Comment API Create  |
| 08 | api/v1/comments/:id        | Comment API Details |
| 09 | api/v1/comments/:id/update | Comment API Update  |
| 10 | api/v1/comments/:id/delete | Comment API Delete  |
