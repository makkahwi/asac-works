# Lesson 27 Reading

Navigation | [Past Reading](../Read-26/README.md) | [Home Page](../README.md) | [Next Reading](../Read-28/README.md) |

## Django Models

[Source](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)

Models in web apps are sort of the equivalent of classes in regular coding. Models are to initialize a structure for data objects to be generated and manipulated, but with a bit more features comparing to regular classes, like defining the type of data to be stored in a specific key, maximum length of data to be stored and relations with other models.

The best practice to build app models is to draft a DB-ERD, which is to contain all models structure (data key, type & features like uniqueness), and the relations between those models.

![DB-ERD](./DB-ERD.jpg)

Once that diagram is built n finilized, models coding is next to build as follows...
from django.db import models
from django.urls import reverse

    class MyModelName(models.Model):

        my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

        class Meta:
            ordering = ['-my_field_name']

        def get_absolute_url(self):
            return reverse('model-detail-view', args=[str(self.id)])

        def __str__(self):
            return self.my_field_name

---

## Django Admin

[Source](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)

Django admin is a built-in feature that provides a pre-built admin panel (panel for system admin with full access to all models data and more). But in order to enlist the built models in the admin panel, they need to be registered in admin.py as follows...

    from .models import Model1, Model2, Model3

    admin.site.register(Model1)
    admin.site.register(Model2)
    admin.site.register(Model3)

Now once the django app is initiazetd, a super user / root user / admin user need to be created so they would have access to the admin panel. It's to be built using the below CLI command and to follow instructions to create a username, email address n password for the super user.

    python3 manage.py createsuperuser

Once the models are registered, admin user is created and server is running, it's possible now to login to admin panel through the default URL of <http://127.0.0.1:8000/admin> using created user credentials. At the point, the registered models would appear following the relevant app, and it's possible to CRUD data from that admin panel. Beside the CRUD of built, migrated & registered models, there are other features a super admin is allowed to do like customizing the outlook of the model controllers like adding filters to model data view, customizing the data detail listing and many more features.
