# Stacks and Queues Pseudo

Advanced engagement of stack and queue as linked lists

## Challenge

Build a linked list as queue, but thourgh stack instances

## Approach & Efficiency

Engage two stacks within PseudoQueue class. To enqueue, value you will be enqueued by using push instance of the first stack. To dequeue, first stack to be pushed into second stack and follow it by pop instance of second stack.

Enqueue time Big(o): o(1)
Enqueue space Big(o): o(1)
Dequeue time Big(o): o(n)
Dequeue space Big(o): o(n)

## API

- Stack Methods...
  1- push: to add new node to the top of the stack
  2- pop: to remove the top node of the stack
  3- peek: to return the value of the top of the stack
  4- is_empty: to check if the given stack is empty or not
  5- to_string: to convert the stack to a text (for test purposes)

- PseudoQueue Methods...
  1- enqueue: to add new node to the rear of the queue (using push instance of stack)
  2- dequeue: to remove the front node of the queue (using push & pop instances of stack)
