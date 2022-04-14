class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise Exception("Empty Stack")
        else:
            holder = self.top
            self.top = self.top.next
            holder.next = None
            return holder.value

    def peek(self):
        if self.top is None:
            raise Exception("Empty Stack")

        return self.top.value

    def is_empty(self):
        return not self.top

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


if __name__ == "__main__":
    pass
