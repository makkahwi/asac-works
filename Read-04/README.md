# Lesson 4 Reading

Navigation
| [Past Reading](../Read-03/README.md) | [Home Page](../README.md) | [Next Reading](../Read-05/README.md) |
| ------------ | --------- | ------------ |

## Classes and Objects

*[Source](https://www.learnpython.org/en/Classes_and_Objects)*

Classes are sort of code structuring to produce pieces of data with similar structures, features and controlling tools. Those pieces produced through classes are what called as objects. So in other words, classes are reached only to create objects according to the coded class and required data / actions.

In python, the classes need to have an initialization method "__init__" to define the data structure of the produced objects. Beside any desired number of methods to reach and manipulate the data.

---

## Thinking Recursively

*[Source](https://realpython.com/python-thinking-recursively/)*

Recursion is what occurs when a method (function) call for itself, or when two methods keep calling each other. So in the case the method is called a recursive method / function.

Recursive methods' main advantage is the caused reduction of coding effort (spare code repeating), as well as lowering space & time consumption sometimes (depends on the algorithm involved). So in the case of having data that should go through a series of behaviors repeatedly and conditionally, recursive methods implementation should be considered.

---

## Pytest Fixtures and Coverage

*[Source](https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage)*

In most of the times while coding test for a python software, most likely that there will be several separate tests for the different parts of the software. Yet the is a good chance to have a common base (starting point) for multiple tests, n here comes the usage of fixtures.

Fixtures in pytest are pieces of codes to initialize a fixed structure of data objects to be used in several tests of a python software.. For example, through this tool an array could be initiated to use with several tests of array manipulation code to add items, search for items, remove items or remove items of the array. So instead of initializing the array with some values in every single test, fixtures provide the solution to only build that array once n use it and whatever tests desired.

As for coverage concept, it's about the answer of the question "how good the existing tests are to really test the coded solution n to check its validity?". It's about building as many interaction & usage scenarios of the solution as possible to test the expected reaction in every diffrect usage.
