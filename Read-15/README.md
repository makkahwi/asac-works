# Lesson 15 Reading

Navigation | [Past Reading](../Read-14/README.md) | [Home Page](../README.md) | [Next Reading](../Read-16/README.md) |

## Trees

[Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)

### Intro

Tree is a data structure of nodes that are linked together in an upside down tree-like form, where trees one root is on the top, and it branches all the way down to the leaves. So in the upside down shape, each node is a parent to the children nodes branching below it.

![Tree](./tree.png)

### Traversals

Trees could be traversed using either a depth first, or bread first approach.

Breadth First is about going through the tree nodes left to right per levels, starting from root level (level 1). So in above figure, tree traversal would be [100,50,200,25,75,155]. This is doable using a Queue.

On the other hand, Depth First is to traverse the tree going into the depth of each branch first. So above figure is to be traversed in this order [100,50,25,75,200,155]. This is to be done using a Stack data structure to trace the nodes.

### Tree Types

There are specific trees that following some rules are categorized into specific types.

- K-ary Tree | Where each parent node could have any number children nodes.
- Binary Tree | Where each parent node has a maximum of two children nodes.
- Binary Search Tree | Where each parent node has a maximum of two children nodes, but the values of nodes need to be order as follows [left child < parent < right child].
