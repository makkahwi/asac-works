class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None

    # Enqueue (add) a node to the queue's rear / tail
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

        return self.to_string()

    # Dequeue (remove) a node of the queue's front
    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue")

        removed = self.front.value
        self.front = self.front.next

        return removed

    # Check if the queue is empty (have no front)
    def is_empty(self):
        return not self.front

    # Convert the queue to text (for testing purposes)
    def to_string(self):
        string = ""

        if self.front == None:
            string = "Queue exists but has no nodes"
        else:
            current = self.front

            while current != None:
                string = string + "{ " + str(current.value) + " }" + " -> "
                current = current.next
            string = string + "None"

        return string


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


class BinarySearchTree(BinaryTree):
    # Add node according to BST Rule (right child is bigger & left child is smaller than parent)
    def add_node(self, value):
        node = BinaryNode(value)
        root = self.root
        current = None

        if self.root == None:
            self.root = node

        while root:
            current = root
            if value < root.value:
                root = root.left
            else:
                root = root.right

        if current == None:
            current = node

        elif value < current.value:
            current.left = node

        else:
            current.right = node


def breadth_first(tree):
    if tree.root == None:
        raise Exception("Empty Tree")

    result = []
    queue = Queue()
    queue.enqueue(tree.root)

    while queue.is_empty() == False:
        if queue.front.value.left:
            queue.enqueue(queue.front.value.left)

        if queue.front.value.right:
            queue.enqueue(queue.front.value.right)

        dequeued = queue.dequeue()
        result.append(dequeued.value)

    return result


if __name__ == "__main__":
    pass
