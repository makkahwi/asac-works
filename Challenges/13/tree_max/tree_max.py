class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    # Push (add) a node to the stack's top
    def push(self, value):
        node = Node(value, self.top)
        self.top = node

        return self.to_string()

    # Push (add) multiple nodes to the stack's top
    def push_multi(self, multi):
        for value in multi:
            node = Node(value, self.top)
            self.top = node

        return self.to_string()

    # Pop (remove) a node of the stack's top
    def pop(self):
        if not self.top:
            raise Exception("Empty Stack")

        removed = self.top.value
        self.top = self.top.next

        return removed

    # Pop (remove) all nodes of the stack's top
    def pop_all(self):
        if not self.top:
            return self

        current = self.top

        while current:
            self.top = self.top.next
            current = self.top

    # Return the node of the stack's top
    def peek(self):
        if not self.top:
            raise Exception("Empty Stack")

        return self.top.value

    # Check if the stack is empty (have no top)
    def is_empty(self):
        return not self.top

    # Convert the stack to text (for testing purposes)
    def to_string(self):
        string = ""

        if self.top == None:
            string = "Stack exists but has no nodes"
        else:
            current = self.top

            while current != None:
                string = string + "{ " + str(current.value) + " }" + " -> "
                current = current.next
            string = string + "None"

        return string


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

    # Enqueue (add) multiple nodes to the queue's rear / tail
    def enqueue_multi(self, multi):
        for value in multi:
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

    # Dequeue (remove) all nodes of the queue's front
    def dequeue_all(self):
        if not self.front:
            raise Exception("Empty Queue")

        while self.front:
            self.front = self.front.next

    # Return the node of the queue's front
    def peek(self):
        if not self.front:
            raise Exception("Empty Queue")

        return self.front.value

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

    # Check the traversal type
    def type(self, type):
        if type == "preorder":
            return self.pre_order(self.root, [])
        elif type == "inorder":
            return self.in_order(self.root, [])
        elif type == "postorder":
            return self.post_order(self.root, [])

    # Pre-order type
    def pre_order(self, node, nodes=[]):
        if node:
            nodes.append(node.value)
            nodes = self.pre_order(node.left, nodes)
            nodes = self.pre_order(node.right, nodes)
        return nodes

    # In-order type
    def in_order(self, node, nodes=[]):
        if node:
            nodes = self.in_order(node.left, nodes)
            nodes.append(node.value)
            nodes = self.in_order(node.right, nodes)
        return nodes

    # Post-order type
    def post_order(self, node, nodes=[]):
        if node:
            nodes = self.in_order(node.left, nodes)
            nodes = self.in_order(node.right, nodes)
            nodes.append(node.value)
        return nodes

    # Get Maximum Value
    def tree_max(self):
        if self.root == None:
            raise Exception("Empty Tree")

        elif self.root.left == None and self.root.right == None:
            return self.root.value

        max = self.root.value

        def search(current):
            nonlocal max

            if current.value > max:
                max = current.value

            if current.left:
                search(current.left)

            if current.right:
                search(current.right)

        search(self.root)

        return max


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

    # Check value existance
    def contains(self, value):
        if self.root == None:
            raise Exception("Empty Tree")

        root = self.root

        while root is not None:
            if value == root.value:
                return True
            if root and value > root.value:
                root = root.right

            if root and value < root.value:
                root = root.left

        return False


if __name__ == "__main__":
    pass
