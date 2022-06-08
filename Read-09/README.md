# Lesson 9 Reading

Navigation

| [Past Reading](../Read-08/README.md) | [Home Page](../README.md) | [Next Reading](../Read-10/README.md) |
| ------------ | --------- | ------------ |

## Dunder Methods

[Source](https://dbader.org/blog/python-dunder-methods)

Dunder is the shortcut for “Double Under (Underscores)”. So dunder / magic methods are methods with two prefix and suffix underscores in their name. Dunder methods are to shape the behavior of the class whenever an operator is called. They are commonly used for operator overloading.

There are some common methods like...

1. __init__
  Used to initialize the data in the class and to define its structure.

2. __str__, __repr__
  Used to represent object data as string / text.

3. __len__, __getitem__, __reversed__
  Used to iterate over the account object

4. __eq__, __lt__
  Used to compare accounts

5. __add__
  Used to merge accounts

6. __call__
  Used to create a callable object

7. __enter__, __exit__
  Used to manage contxt

## Statistics - Probability

[Source](https://www.dataquest.io/blog/basic-statistics-in-python-probability/)

### Probability

Probability means possibility. Probability is the mathematics attempt to predict the chances of an event occurrence, based on collected real data (statistics).

### The data and the distribution

Normal distribution: refers to a particularly important phenomenon in the realm of probability and statistic.
Normal distribution has a unique symmetry and shape when tracked on a graph.

### Revisiting the normal

The normal distribution is significant to probability and statistics, two factors: the Central Limit Theorem and the Three Sigma Rule.

Central Limit Theorem Central Limit Theorem lets us know that the average of many trials means will approach the true mean, Three Sigma Rule Three Sigma Rule will tell us how much the data will be spread out around this mean.

Z-score The Z-score is a simple calculation that answers the question, “Given a data point, how many standard deviations is it away from the mean?” The equation below is the Z-score equation.
