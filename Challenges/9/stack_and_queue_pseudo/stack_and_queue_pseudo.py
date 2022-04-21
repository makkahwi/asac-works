class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    # Push (add) a node to the stack's top
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    # Pop (remove) a node of the stack's top
    def pop(self):
        if self.top is None:
            raise Exception("Empty Stack")
        else:
            holder = self.top
            self.top = self.top.next
            holder.next = None
            return holder.value

    # Return the node of the stack's top
    def peek(self):
        if self.top is None:
            raise Exception("Empty Stack")

        return self.top.value

    # Check if the stack is empty (have no top)
    def is_empty(self):
        return not self.top

    # Convert the stack to text (for testing purposes)
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

    # Enqueue (add) a node to the queue's rear / tail
    def enqueue(self, value):
        self.enq.push(value)

        if self.deq.top == None:
            while not self.enq.top == None:
                self.deq.push(self.enq.pop())

    # Dequeue (remove) a node of the queue's front
    def dequeue(self):
        if self.deq.top == None and self.enq.top == None:
            raise (Exception("Pseudo Queue is empty!"))

        elif self.deq.top == None and not self.enq.top == None:
            while not self.enq.top == None:
                self.deq.push(self.enq.pop())
            return self.deq.pop()

        else:
            return self.deq.pop()


if __name__ == "__main__":
    pass
