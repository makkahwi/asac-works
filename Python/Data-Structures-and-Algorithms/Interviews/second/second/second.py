class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.header = None

    # Add a node to linked list
    def insert(self, value):
        node = Node(value, self.header)
        self.header = node

    # Add a node to linked list end / tail / rear
    def insert_at_tail(self, value):
        if self.header == None:
            self.header = Node(value, None)
        else:
            current = self.header
            while current.next != None:
                current = current.next
            else:
                current.next = Node(value, None)

    # Add multiple nodes to linked list end / tail / rear
    def insert_multi(self, nodes):
        for node in nodes:
            self.insert_at_tail(node)

        return nodes

    # Get list length
    def length(self):
        length = 0
        current = self.header

        while current != None:
            length = length + 1
            current = current.next

        return length

    # Remove a node
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

    # Add a node to a spacific position of a linked list
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

    # Check if a node is part of a linked list
    def includes(self, value):
        current = self.header

        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False

    # Convert a linked list to text (for checking purposes)
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


def checkLinkedList(list):
    result = True
    list = []
    middle = 0
    current = list.head

    while current:
        list.append(current.value)
        current = current.next

    # list = [1,2,3,4,5]
    if int(len(list) % 2) == 0:
        middle = int(len(list) / 2)
    else:
        middle = int(len(list) / 2) + 1

    i = 0

    while i < middle:
        if list[i] == list[len(list) - 1 - i]:
            result = True
        else:
            return False

        i += 1

    return result
