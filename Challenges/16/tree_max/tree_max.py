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
