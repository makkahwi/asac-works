# django-snacks

LTUC's Django First Project

## How to recreate

1. Run following CLI commands

- poetry new [django-snacks]
- poetry install
- poetry shell
- poetry add django
- django-admin startproject [snacks_project] OR [snack_tracker_project]
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

- "/" | Snacks List (Home Page)
- "/:id" | Snack Details
- "/about" | About Page
