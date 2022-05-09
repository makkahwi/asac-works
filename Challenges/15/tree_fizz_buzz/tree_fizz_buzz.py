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


# Fizz Buzz Node Check
def check(node):
    if int(node.value) % 3 == 0 and int(node.value) % 5 == 0:
        node.value = "FizzBuzz"
    elif int(node) % 3 == 0:
        node.value = "Fizz"
    elif int(node) % 5 == 0:
        node.value = "Buzz"
    else:
        node.value = str(node.value)


# Go Though Children Nodes
def looping(node):
    for child in node.children:
        check(child)
        if len(child.children):
            looping(child)


# Fizz Buzz Main Function
def fizz_buzz_tree(tree):
    node = tree.root

    check(node)
    looping(node)

    return tree


if __name__ == "__main__":
    pass
