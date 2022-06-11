# Lesson 34 Reading

Navigation | [Past Reading](../Read-33/README.md) | [Home Page](../README.md) | [Next Reading](../Read-35/README.md) |

## Django Settings Best Practices

[Source](https://djangostars.com/blog/configuring-django-settings-best-practices/)

Issues might be faced...

- Different environments | In a web dev, it's always the best practice to have several envs for the several stages of build the project, like development env, production env & local env. Each would have own configs & settings to fit the purpose of the env and make most of it.

- Sensitive data | There always will be data that can't be shared like passwords & sercret keys. In such cases, the unshared files of .env are built to host store them in relevant envs without exposing them to the non authorized.

- Sharing Settings | While a development team is building a project, there are some settings that only those team members need to be aware of. So it's a trick situation of closed-circle share need.

The very best solution to overcome those issues is to involve *django-environ*. It's a library that deals the above-listed security and variety issues and provides an almost perfect solution for each of them.

---

## SSH Tutorial

[Source](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

Text
