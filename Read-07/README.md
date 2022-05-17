# Lesson 7 Reading

## Python Scopes

[Source](https://realpython.com/python-scope-legb-rule/)

The concepts of global scopes and names in Python are inextricably linked to module files. Wehn declaring a name at the top level of a Python file, the name is regarded global to that file and it's child parts. This is why this type of scope is also known as module scope.

Nonlocal names on the other hand can be retrieved from inner functions in the same way as global names can, but they cannot be assigned or changed. You must use a nonlocal statement if you want to change them.

Namespaces refer to Python scopes which are dictionaries that associate names to objects

LEGB Rule which is about the process of locating names of python.

- Local scope
- Enclosing Scope
- Global Scope
- Built-In Scope
