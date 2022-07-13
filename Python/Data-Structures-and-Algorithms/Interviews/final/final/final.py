class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        node = Node(value)

        if self.front:
            current = self.front

            while current.next:
                current = current.next
            else:
                current.next = node
        else:
            self.front = node

    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue")

        removed = self.front.value
        self.front = self.front.next

        return removed

    def is_empty(self):
        return not self.front


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def tree_mirroring(bt):
    if not bt.root:
        raise Exception("Tree is empty")

    if not bt.root.left and not bt.root.right:
        return bt

    queue = Queue()
    queue.enqueue(bt.root)

    while not queue.is_empty():
        if queue.front.left and queue.front.right:
            temp = queue.front.left
            queue.front.left = queue.front.right
            queue.front.right = temp
            queue.enqueue(queue.front.right)
            queue.enqueue(queue.front.left)

        elif queue.front.left:
            queue.front.right = queue.front.left
            queue.front.left = None
            queue.enqueue(queue.front.right)

        elif queue.front.right:
            queue.front.left = queue.front.right
            queue.front.right = None
            queue.enqueue(queue.front.left)

        queue.dequeue()

    return bt
