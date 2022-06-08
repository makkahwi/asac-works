# Lesson 8 Reading

Navigation
| [Past Reading](../Read-07/README.md) | [Home Page](../README.md) | [Next Reading](../Read-09/README.md) |
| ------------ | --------- | ------------ |

## List Comprehensions

[Source](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

List comprehension offers an option to create a new list based on values of an existing list without involving loops. It's a shorter syntax which helps to minimize coding effort and provide a more readable code.

List comprehension could have countless uses. Here are some examples...

1. It could be used to create list with some customization, like creating a range of even numbers only...

    digits = [x for x in range(10) if x % 2 == 0]

    """
    Note that above code is the shortcut of using a loop as follows.
    """

    digits = []

    for x in range(10):
      if x % 2 == 0:
        digits.append(x)

2. To create a new list that is the result of multiplying 5 by old list items, it would be coded as below.

    newlist = [ element**5 for element in oldlist ]

    """
    Note that above code is the shortcut of using a loop as follows.
    """

    newlist = []

    for element in oldlist:
      newlist.append(element*5)

3. Get first letter of array of texts.

    texts = ["Terrible event", "Emotional response", "Xenophobia", "Trauma"]

    letters = [ text[0] for text in texts ]

    """
    Note that above code is the shortcut of using a loop as follows.
    """

    texts = ["Terrible event", "Emotional response", "Xenophobia", "Trauma"]

    letters = []

    for text in texts:
      letters.append(text[0])
