# django-snacks

LTUC's Django First Project

## How to recreate

1. Run following CLI commands
    - poetry new [snacks-crud]
    - cd [snacks-crud]
    - poetry install
    - poetry shell
    - poetry add django
    - django-admin startproject [snacks_crud_project]
    - cd [snacks_crud_project]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [snacks]

2. Create your models
    - Add models construction in [snacks]/models.py
    - Add [snacks] to INSTALLED_APPS list in [snacks_crud_project]/settings.py
    - Register model in [snacks]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Create your templates & views
    - Create your view files in [snacks_crud_project]/templates
    - Add "BASE_DIR / 'templates'" as value of "DIRS" in TEMPLATES list in [snacks_crud_project]/settings.py
    - Add "STATICFILES_DIRS" list in [snacks_crud_project]/settings.py
    - Create urls.py in [snacks] directory.
    - Add & link views to desired URLs in urls.py
    - Link views in [snacks]/views.py to approprate built-in view type & related model

## How to start

- python manage.py runserver

## How to test

- python manage.py test

## APIs

- "/" | Snacks List (Home Page)
- "/:id" | Snack Details
- "/about" | About Page
