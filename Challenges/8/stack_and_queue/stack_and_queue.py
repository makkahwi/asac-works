class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

        return self.to_string()

    def push_multi(self, multi):
        for value in multi:
            node = Node(value, self.top)
            self.top = node

        return self.to_string()

    def pop(self):
        if not self.top:
            raise Exception("Empty Stack")

        removed = self.top.value
        self.top = self.top.next

        return removed

    def pop_all(self):
        if not self.top:
            return self

        current = self.top

        while current:
            self.top = self.top.next
            current = self.top

    def peek(self):
        if not self.top:
            raise Exception("Empty Stack")

        return self.top.value

    def is_empty(self):
        return not self.top

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

    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue")

        removed = self.front.value
        self.front = self.front.next

        return removed

    def dequeue_all(self):
        if not self.front:
            raise Exception("Empty Queue")

        while self.front:
            self.front = self.front.next

    def peek(self):
        if not self.front:
            raise Exception("Empty Queue")

        return self.front.value

    def is_empty(self):
        return not self.front

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


if __name__ == "__main__":
    pass