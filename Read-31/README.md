# Lesson 31 Reading

## Docker

[Source](https://wsvincent.com/beginners-guide-to-docker/)

Containerization concept is about wrapping up an app in an isolated & duplicable environment. It's to come over the issues resulted by using various working environments (like the OSs of Windows, Linux & Mac AND global packages like Python, Node.js ...etc).

Virtual environment on the other hand is a simpler concept, as it's about isolating a Python project packages locally, which sounds like a containerization. But the global installation are the base to the virtual environment, n when a package is added to the virtual environment, it needs to be added to the global installation first. So, virtual environment is not a total seperation from local machine like containerization.

Docker is a complex linux-based containerization and virtualization tech. Its two main concepts are images & containers. Images are the mirroring of a project @ a certain time, while containers are the live run of those images. Images are mostly used to import / pull pre-built environments & setups, like database systems & database UI, as well as retrieving a backup of a container.

When an image is imported or a container is initiated it needs a first-time setup (pulling any needed setups & packages) & build. Once they're built, main commands would be about running up, shutting down and restarting the containers on need.

---

## Django APIs

[Source](https://djangoforapis.com/library-website-and-api/)

Text
