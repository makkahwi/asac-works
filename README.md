# Django REST API Framework

LTUC Django-Based Project

## How to recreate

1. Run following CLI commands
    - poetry new [dj-snacks-rest]
    - cd [dj-snacks-rest]
    - poetry install
    - poetry shell
    - poetry add django django-filter djangorestframework Markdown
    - django-admin startproject [dj_snacks_rest_api]
    - cd [dj_snacks_rest_api]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [snacks]

2. Create your models
    - Add models construction in [snacks]/models.py
    - Add [snacks] to INSTALLED_APPS list in [dj_snacks_rest_api]/settings.py
    - Register model in [snacks]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Create your template & views
    - Create your view files in [dj_snacks_rest_api]/templates
    - Add "BASE_DIR / 'templates'" as value of "DIRS" in TEMPLATES list in [dj_snacks_rest_api]/settings.py
    - Add "STATICFILES_DIRS" list in [dj_snacks_rest_api]/settings.py
    - Create urls.py in [snacks] directory.
    - Add & link views to desired URLs in urls.py
    - Link views in [snacks]/views.py to approprate built-in view type & related model

5. Do REST API configs
    - Add "rest_framework" to INSTALLED_APPS list in [dj_snacks_rest_api]/settings.py
    - Add default rest configs in tail of [dj_snacks_rest_api]/settings.py
        REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
    - Create [snacks]/api/serializers.py & link models
    - Create [snacks]/api/viewset.py & link models & serializers
    - Add API URLs to [snacks]/urls.py

## How to start

- python manage.py runserver

## APIs

### CRUD

- "/" | Snack List
- "snacks/create" | Snack Create
- "snacks/:id" | Snack Details
- "snacks/:id/update" | Snack Update
- "snacks/:id/delete" | Snack Delete
- "/about" | About Page

### REST API

- "api/v1/snacks" | Snacks API List
- "api/v1/snacks/create" | Snack API Create
- "api/v1/snacks/:id" | Snack API Details
- "api/v1/snacks/:id/update" | Snack API Update
- "api/v1/snacks/:id/delete" | Snack API Delete
