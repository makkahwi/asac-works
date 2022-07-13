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


def breadth_first(tree):
    arr = []

    q = Queue()
    q.enqueue(tree.root)

    while not q.is_empty():
        if q.front.left.value:
            q.enqueue(q.front.left.value)

        if q.front.right.value:
            q.enqueue(q.front.right.value)

        arr.append(q.front)
        q.deqeueu()

    return arr


def sum_odds(self):
    result = 0

    for node in breadth_first(self):
        if node % 2 != 0:
            result += node

    return result
