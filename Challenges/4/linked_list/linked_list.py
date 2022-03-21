class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.header = None

    def insert(self, value):
        node = Node(value, self.header)
        self.header = node

    def insert_at_tail(self, value):
        if self.header == None:
            self.header = Node(value, None)
        else:
            current = self.header
            while current.next != None:
                current = current.next
            else:
                current.next = Node(value, None)

    def insert_multi(self, nodes):
        for node in nodes:
            self.insert_at_tail(node)

        return nodes

    def length(self):
        length = 0
        current = self.header

        while current != None:
            length = length + 1
            current = current.next

        return length

    def remove_node(self, i):
        if i >= self.length() or i < 0:
            raise Exception("Invalid Index")

        elif i == 0:
            self.header = self.header.next

        length = 0
        current = self.header

        while current != None:
            if length == i - 1:
                current.next = current.next.next
                break

            current = current.next
            length = length + 1

    def insert_at(self, i, value):
        if i >= self.length() or i < 0:
            raise Exception("Invalid Index")

        elif i == 0:
            self.insert(value)

        length = 0
        current = self.header

        while current != None:
            if length == i - 1:
                node = Node(value, current.next)
                current.next = node
                break
            current = current.next
            length = length + 1

    def includes(self, value):
        current = self.header

        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False

    def to_string(self):
        string = ""

        if self.header == None:
            string = "List exists but has no nodes"
        else:
            current = self.header

            while current != None:
                string = string + "{ " + str(current.value) + " }" + " -> "
                current = current.next
            string = string + "None"

        return string


if __name__ == "__main__":
    pass
