# Lesson 5 Reading

Navigation
| [Past Reading](../Read-04/README.md) | [Home Page](../README.md) | [Next Reading](../Read-07/README.md) |
| ------------ | --------- | ------------ |

## Big O

*[Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/big_oh.html)*

Big O is an indicator to the complexity of a problem solution for specific criteria like time consumption of space usage. It actually indicate the worst case scenarios of using the algorithm. The major concerns to indicate are the time complexity and space complexity. The process of analyzing either complexity includes considering 4 relevant factors of the algorithm. Those factors are input type & size, measurement units, growth order and the 3 cases (best, average and worst).

---

## Linked List

*[Source 1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html)*
*[Source 2](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)*
*[Source 3](https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996)*

Linked list is a chains of nodes that are stored seperatrly in the memory of a machine. To have the list, each node should have a pointer to the next node or to null in case of last node of the list. First item of the list is mostly referred to as the head of the list.

In case of having nodes with only 1 pointer to 1 node, the list would be called as linear list. And when the linear list last node point to null, the list would be referred to as Singly Linked List as nodes could be approached only from head to tail. In case of having the linear list but last node points to the list head, it would be called as Circular Linked List.

In other cases, the pointer could point to more than 1 node and called non-linear. Non-linear nodes could point to the previous & next node, so the list could be approached from tail to head or from head to tail (Doubly Linked List). And in some cases, a node could point to multiple text nodes to form what is called a Tree.
