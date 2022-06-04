class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Push (add) a node to the stack's top

        Args:
            a stack & a value for new node

        Returns:
            the stack with new node at top

        """
        node = Node(value, self.top)
        self.top = node

        return self.to_string()

    def push_multi(self, multi):
        """
        Push (add) multiple nodes to the stack's top

        Args:
            a stack & values for new nodes

        Returns:
            the stack with new nodes at top

        """
        for value in multi:
            node = Node(value, self.top)
            self.top = node

        return self.to_string()

    def pop(self):
        """
        Pop (remove) a node of the stack's top

        Args:
            a stack

        Returns:
            the stack without top node

        """
        if not self.top:
            raise Exception("Empty Stack")

        removed = self.top.value
        self.top = self.top.next

        return removed

    def pop_all(self):
        """
        Pop (remove) all nodes of the stack's top

        Args:
            a stack

        Returns:
            the stack without nodes

        """
        if not self.top:
            return self

        current = self.top

        while current:
            self.top = self.top.next
            current = self.top

    def peek(self):
        """
        Return the node of the stack's top

        Args:
            a stack

        Returns:
            the stack’s top value

        """
        if not self.top:
            raise Exception("Empty Stack")

        return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty (have no top)

        Args:
            a stack

        Returns:
            boolean for stack having no top

        """
        return not self.top

    def to_string(self):
        """
        Convert the stack to text (for testing purposes)

        Args:
            a stack

        Returns:
            stack's nodes printed in a text string

        """
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

    def enqueue(self, value):
        """
        Enqueue (add) a node to the queue's rear / tail

        Args:
            a queue & a value for new node

        Returns:
            the queue with new node at tail

        """
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

    def enqueue_multi(self, multi):
        """
        Enqueue (add) multiple nodes to the queue's rear / tail

        Args:
            a queue & values for new nodes

        Returns:
            the queue with new nodes at tail

        """
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

    def dequeue(self):
        """
        Dequeue (remove) a node of the queue's front

        Args:
            a queue

        Returns:
            the queue without front node

        """
        if not self.front:
            raise Exception("Empty Queue")

        removed = self.front.value
        self.front = self.front.next

        return removed

    def dequeue_all(self):
        """
        Dequeue (remove) all nodes of the queue's front

        Args:
            a queue

        Returns:
            the queue without nodes

        """
        if not self.front:
            raise Exception("Empty Queue")

        while self.front:
            self.front = self.front.next

    def peek(self):
        """
        Return the node of the queue's front

        Args:
            a queue

        Returns:
            the queue front value

        """
        if not self.front:
            raise Exception("Empty Queue")

        return self.front.value

    def is_empty(self):
        """
        Check if the queue is empty (have no front)

        Args:
            a queue

        Returns:
            boolean for queue having no front

        """
        return not self.front

    def to_string(self):
        """
        Convert the queue to text (for testing purposes)

        Args:
            a queue

        Returns:
            queue's nodes printed in a text string

        """
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

    def type(self, type):
        """
        Check the traversal type

        Input:
        String

        Output:
        None
        """

        if type == "preorder":
            return self.pre_order(self.root, [])
        elif type == "inorder":
            return self.in_order(self.root, [])
        elif type == "postorder":
            return self.post_order(self.root, [])

    def pre_order(self, node, nodes=[]):
        """
        To do pre-order traversal

        Input:
        New node, list of nodes

        Output:
        List of nodes
        """
        if node:
            nodes.append(node.value)
            nodes = self.pre_order(node.left, nodes)
            nodes = self.pre_order(node.right, nodes)
        return nodes

    def in_order(self, node, nodes=[]):
        """
        To do in-order traversal

        Input:
        New node, list of nodes

        Output:
        List of nodes
        """
        if node:
            nodes = self.in_order(node.left, nodes)
            nodes.append(node.value)
            nodes = self.in_order(node.right, nodes)
        return nodes

    def post_order(self, node, nodes=[]):
        """
        To do post-order traversal

        Input:
        New node, list of nodes

        Output:
        List of nodes
        """
        if node:
            nodes = self.in_order(node.left, nodes)
            nodes = self.in_order(node.right, nodes)
            nodes.append(node.value)
        return nodes


class BinarySearchTree(BinaryTree):
    def add_node(self, value):
        """
        Add node according to BST Rule (right child is bigger & left child is smaller than parent)

        Input:
        New node value

        Output:
        None
        """
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

    def contains(self, value):
        """
        Check value existance

        Input:
        Node value to check

        Output:
        Boolean of node exsitance
        """
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
