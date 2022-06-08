# Lesson 10 Reading

Navigation

| [Past Reading](../Read-09/README.md) | [Home Page](../README.md) | [Next Reading](../Read-11/README.md) |
| ------------ | --------- | ------------ |

## Stacks and Queues

[Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)

### Stacks

A stack is a data structure that stores nodes in one-way link, built with first-in last-out approach. Meaning that nodes are approachable only by going through them one-by-one starting at the first node. And whatever methods to apply, they only apply to the most-recent added node (top node).

A Stack Visualization

|        |
| Node 3 | Top Node
| Node 2 |
| Node 1 |
| ------ |

Basic Stack's Node Structure

{
  value: Node 1
  pointer: "points to next node"
}

Basic methods to handle stacks...

1. push: to add nodes to stack's top
2. pop: to remove the stack's top node

### Queues

A queue is a data structure that stores nodes in one-way link, built with first-in first-out approach. Meaning that nodes are approachable only by going through them one-by-one starting at the first node. And the available methods could apply to the most-recent added node (rear node) or the first added node (front node).

A Queue Visualization

Front Node         Rear Node
| ------ | ------ | ------ |
| Node 1 | Node 2 | Node 3 |
| ------ | ------ | ------ |

Basic Queue's Node Structure

{
  value: Node 1
  pointer: "points to next node"
}

Queue nodes could be built to be two-way approached. So it would have two pointers to point to next and previous nodes.

Queue's Two-Way Node Structure

{
  value: Node 1
  pointer1: "points to previous node"
  pointer2: "points to next node"
}

Basic methods to handle queues...

1. enqueue: to add nodes to stack's rear
2. dequeue: to remove the stack's front node
