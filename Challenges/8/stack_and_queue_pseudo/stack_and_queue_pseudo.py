class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        node = Node(value, self.list)
        self.list.append(node)

    def pop(self):
        if not self.list:
            raise Exception("Empty Stack")

        self.list.pop()

    def peek(self):
        if not self.list:
            raise Exception("Empty Stack")

        return self.list.value

    def is_empty(self):
        return not self.list

    def to_string(self):
        string = ""

        if self.list == None:
            string = "Stack exists but has no nodes"
        else:
            current = self.list

            while current != None:
                string = string + "{ " + str(current.value) + " }" + " -> "
                current = current.next
            string = string + "None"

        return string


class PseudoQueue:
    def __init__(self):
        self.enq = Stack()
        self.deq = Stack()

    def enqueue(self, value):
        self.enq.push(value)

        return value

    def dequeue(self):
        if not self.deq.is_empty():
            raise Exception("Empty Queue")

        removed = self.deq.push(self.enq.pop())

        return removed


if __name__ == "__main__":
    pass
