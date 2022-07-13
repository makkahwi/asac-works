class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def tree_max(self):
        """
        To find the maximum node value

        Input:
        None

        Output:
        Return maximum value
        """

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


if __name__ == "__main__":
    pass
