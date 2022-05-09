class tree_node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = []

        if children != None:
            for child in children:
                self.children.append(tree_node(child))


class k_ary_tree:
    def __init__(self):
        self.root = None

    # Add nodes to the tree
    def add_node(self, node, children=None):
        if not self.root or self.root.value == node:
            self.root = tree_node(node, children)
        else:
            current = self.root

            while current:
                for child in current.children:
                    if child.value == node:
                        child = tree_node(node, children)

                current = current.children[0]


if __name__ == "__main__":
    pass
