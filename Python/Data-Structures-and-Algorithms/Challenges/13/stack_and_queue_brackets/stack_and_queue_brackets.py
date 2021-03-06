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


def validate_brackets(input):
    if input == None:
        raise Exception("Empty input")

    stack = Stack()
    new = ""

    for x in input:
        if x == "(" or x == ")" or x == "[" or x == "]" or x == "{" or x == "}":
            new += x

    if new != "":
        for letter in new:
            if letter == "(" or letter == "[" or letter == "{":
                stack.push(letter)

            elif letter == ")" or letter == "]" or letter == "}":
                if stack.is_empty():
                    return False
                else:
                    if (
                        (letter == ")" and stack.peek() == "(")
                        or (letter == "]" and stack.peek() == "[")
                        or (letter == "}" and stack.peek() == "{")
                    ):
                        stack.pop()
                    else:
                        return False
    else:
        raise Exception("No brackets in input")

    if stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    pass
