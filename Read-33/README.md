# Lesson 27 Reading

## JSON Web Tokens

[Source](https://jwt.io/introduction/)

JWT stands for JSON Web Token, which is a sort of a unique signature that signifies the user identity. It's mostly used for accross-app authentication for access restriction cases, but it also could be used for accross-app ciphered data exchange.

JWT creation formula is: [header].[payload/content].[signature]

For accross-app JWT authentication, the standard use is to attach it to the API header as follows: {Authorization: Bearer [token]}

---

## DRF JWT Authentication

[Source](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)

"djangorestframework_simplejwt" is the library to involve JWT in Django REST Framework so authentication could be applied to the API calls. Which should be installed into the project packages & added to the project settings & configs.

In DRF-JWT, the basic two operations are to obtain the token & to refresh it on expiry.

---

## Django Runserver Is Not Your Production Server

[Source](https://build.vsupalov.com/django-runserver-in-production/)

Text
