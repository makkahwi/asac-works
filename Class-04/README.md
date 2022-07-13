# Learning Journal 4

Navigation | [Past Journal](../Class-02/README.md) | [Home Page](../README.md) | [Next Journal](../Class-05/README.md) |

## OOP in Python (Classes) & Fixtures

### What did I learn today?

#### Classes

What are classes and objects & how to build them in Python.

Classes are to be defined or initiated to decide the structure of the class data. Objects are the data resulted by using a class. So classes are basically data structure / template where object is the structured data which could be generated through the class. Classes are to be coded as follows...

  class class_name():
    def __init__(self, value1=default_value, ...):
        self.preperty1 = value1
        .
        .
        .

Classes may contain some methods which are to be applied to the created objects of the class. These methods are be defined as follows within the class...

    def method_name(self,...):
      <logical operations>
      return

Data to create an object & populate it could be fed while initiating a class, or through building a customized add / create / populate method(s).

#### Fixtures

Fixture is a simple concept to be used @ Python poetry tests. It's to initialize some global data which could be imported while testing units.

### What went well, that I might forget if I don’t write down?

It's quite clear. For someone who isn't new to coding, Class is a basic & well-known concept. It's just to practise the classes build so the syntax would be absorbed.

### What still puzzles me, or what do I need to learn more about?

There is only a minor issue with understanding the __ (Dunder Methods) meaning & use. It's only clear @ this point that it's to be used with initialization method.

### What should I do differently next time?

None

### Is the assignment complete? If not, where exactly did you leave off, and what work remains?

Assignment was submitted late but complete and functioning well without issues.
