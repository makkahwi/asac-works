# Lesson 31 Reading

Navigation
| [Past Reading](../Read-30/README.md) | [Home Page](../README.md) | [Next Reading](../Read-32/README.md) |
| ------------ | --------- | ------------ |

## Docker

[Source](https://wsvincent.com/beginners-guide-to-docker/)

Containerization concept is about wrapping up an app in an isolated & duplicable environment. It's to come over the issues resulted by using various working environments (like the OSs of Windows, Linux & Mac AND global packages like Python, Node.js ...etc).

Virtual environment on the other hand is a simpler concept, as it's about isolating a Python project packages locally, which sounds like a containerization. But the global installation are the base to the virtual environment, n when a package is added to the virtual environment, it needs to be added to the global installation first. So, virtual environment is not a total seperation from local machine like containerization.

Docker is a complex linux-based containerization and virtualization tech. Its two main concepts are images & containers. Images are the mirroring of a project @ a certain time, while containers are the live run of those images. Images are mostly used to import / pull pre-built environments & setups, like database systems & database UI, as well as retrieving a backup of a container.

When an image is imported or a container is initiated it needs a first-time setup (pulling any needed setups & packages) & build. Once they're built, main commands would be about running up, shutting down and restarting the containers on need.

---

## Django APIs

[Source](https://djangoforapis.com/library-website-and-api/)

"DjangoRestFramework" is the library to involve REST API (URL endpoints to exchange data in JSON format) calls in a Django-based project.

Steps to engage REST APIs in Django are as follows...

1. To build a traditional Django project, run following CLI commands
    - poetry new [dj-project]
    - cd [dj-project]
    - poetry install
    - poetry shell
    - poetry add django django-filter djangorestframework Markdown
    - django-admin startproject [dj_project]
    - cd [dj_project]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [application]
    - Add [application] to INSTALLED_APPS list in [dj_project]/settings.py

2. Build your models
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
