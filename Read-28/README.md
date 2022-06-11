# Lesson 28 Reading

Navigation | [Past Reading](../Read-27/README.md) | [Home Page](../README.md) | [Next Reading](../Read-29/README.md) |

## Django Forms

[Source](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)

Forms are pre-built data containers, which are basically used to collect structured and organized data from user as an input to be passed to the machine for processes. Usually, there is a minimum of 1 form for each model built in a web app, built to handle the data CRUD including the data structure specified in the model.

Django handles forms in a bit more complex way than regular HTML forms

- First, it presents the default form the first time it is called by the user.
- Then, collects submitted data and bind it to the form.
- Then it cleans and validate (check if it meets specific rules like type & length) the data. If validation isn't passed, it returns the populated form with error messages for the problems found.
- If validation is passed, it performs the required actions (like storing the data, send an email, return the result of a search, upload a file ...etc).
- Once all above steps are done, it redirects user to a specific page.

![Django-Form-Handling-Proccess](./django-forms.png)
