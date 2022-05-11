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


class tree_node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


# Fizz Buzz Node Check
def check(node):
    if node.value % 3 == 0 and node.value % 5 == 0:
        node.value = "FizzBuzz"
    elif node.value % 3 == 0:
        node.value = "Fizz"
    elif node.value % 5 == 0:
        node.value = "Buzz"
    else:
        node.value = str(node.value)


# Go Though Children Nodes
def looping(node):
    for child in node.children:
        check(child)
        if child.children:
            looping(child)


class k_ary_tree:
    def __init__(self, root=None):
        self.root = root

    # Fizz Buzz Main Function
    def fizz_buzz_tree(self):
        if self.root:
            node = self.root

            check(node)
            looping(node)

            return self
        else:
            return Exception("Empty Tree")

    # Breadth First Tree Listing
    def breadth_first(self):
        if self.root == None:
            raise Exception("Empty Tree")

        result = []
        queue = Queue()
        queue.enqueue(self.root)

        while queue.is_empty() == False:
            for child in queue.front.value.children:
                queue.enqueue(child)

            dequeued = queue.dequeue()
            result.append(dequeued.value)

        return result


if __name__ == "__main__":
    pass
