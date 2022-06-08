# Lesson 32 Reading

Navigation

| [Past Reading](../Read-31/README.md) | [Home Page](../README.md) | [Next Reading](../Read-33/README.md) |
| ------------ | --------- | ------------ |

## DRF Permissions

[Source](https://www.django-rest-framework.org/api-guide/permissions/)

In a nutshell, permissions are about whether a specific user or a group of users are allowed to access a specific endpoint (to create, read, update, delete or any other ops). Typically, permission check is triggered once an endpoint is called before any processes of the endpoint start. If access is granted, the processes would resume as normal, otherwise it would return a 403 error code.

In REST frameworks, permissions are defined as classes, which to be accessed right before retrieving a view. Permissions could be applied to be model-level or object-level.

Permission types:

- AllowAny: grants unrestricted access.
- IsAuthenticated: restrict any access to allowed users only.
- IsAdminUser: allow only admin users (defined as user.is_staff).
- IsAuthenticatedOrReadOnly: restrict any non-read access to allowed users only.
- DjangoModelPermissions: deny any access to users which aren't allowed to access the model.
- DjangoModelPermissionsOrAnonReadOnly: deny non-read access to users which aren't allowed to access the model.
- DjangoObjectPermissions: deny any access to users which aren't allowed to access the object.
- Custom permissions: to build own access based on own needs.

Useful 3rd party Packages:

- DRF
- Composed Permissions
- REST Condition
- DRY REST Permissions
- Django Rest Framework Roles
- Django REST Framework API Key
- Django Rest Framework Role Filters
- Django Rest Framework PSQ
