# drf-api

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

2. Create your models, templates & views

3. Run following CLI commands

- python manage.py makemigrations
- python manage.py migrate

## How to start

- python manage.py runserver

## APIs

- "/" | Home Page
