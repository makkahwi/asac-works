class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


def breadth_first(tree):
    if tree.root == None:
        raise Exception("Empty Tree")

    result = []
    queue = Queue()
    queue.enqueue(tree.root)

    while queue.is_empty() == False:
        left = None
        right = None

        if queue.front.value.left:
            queue.enqueue(queue.front.value.left)
            left = queue.front.value.left.value

        if queue.front.value.right:
            queue.enqueue(queue.front.value.right)
            right = queue.front.value.right.value

        result.append({"parent": queue.front.value, "left": left, "right": right})
        queue.dequeue()

    return result


def compare_trees(tree1, tree2):
    list1 = breadth_first(tree1)
    list2 = breadth_first(tree2)

    if len(list1) != len(list2):
        return False

    length = len(list1)

    for i in range(0, length - 1):
        if list1[i]["parent"] != list2[i]["parent"]:
            return False
        elif list1[i]["left"] != list2[i]["left"]:
            return False
        elif list1[i]["right"] != list2[i]["right"]:
            return False

    return True
