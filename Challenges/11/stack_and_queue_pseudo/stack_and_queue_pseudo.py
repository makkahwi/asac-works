class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Push (add) a node to the stack's top

        Args:
            a stack & a value for new node

        Returns:
            the stack with new node at top

        """
        node = Node(value)
        node.next = self.top
        self.top = node

        return self.to_string()

    def pop(self):
        """
        Pop (remove) a node of the stack's top

        Args:
            a stack

        Returns:
            the stack without top node

        """
        if self.top is None:
            raise Exception("Empty Stack")
        else:
            holder = self.top
            self.top = self.top.next
            holder.next = None
            return holder.value

    def peek(self):
        """
        Return the node of the stack's top

        Args:
            a stack

        Returns:
            the stack’s top value

        """
        if self.top is None:
            raise Exception("Empty Stack")

        return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty (have no top)

        Args:
            a stack

        Returns:
            boolean for stack having no top

        """
        return not self.top

    def to_string(self):
        """
        Convert the stack to text (for testing purposes)

        Args:
            a stack

        Returns:
            stack's nodes printed in a text string

        """
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


class PseudoQueue:
    def __init__(self):
        self.enq = Stack()
        self.deq = Stack()

    def enqueue(self, value):
        """
        Enqueue (add) a node to the queue's rear / tail

        Args:
            a queue & a value for new node

        Returns:
            the queue with new node at tail

        """
        self.enq.push(value)
        return self.enq.to_string()

    def dequeue(self):
        """
        Dequeue (remove) a node of the queue's front

        Args:
            a queue

        Returns:
            the queue without front node

        """
        if self.enq.top == None:
            raise (Exception("Pseudo Queue is empty!"))

        else:
            while self.enq.top != None:
                self.deq.push(self.enq.pop())
            return self.deq.pop()


if __name__ == "__main__":
    pass
