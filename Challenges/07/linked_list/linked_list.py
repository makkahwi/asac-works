class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.header = None

    # Add a node to linked list top
    def insert(self, value):
        node = Node(value, self.header)
        self.header = node

    # Add a node to linked list tail
    def append(self, value):
        if self.header == None:
            self.header = Node(value, None)
        else:
            current = self.header
            while current.next != None:
                current = current.next
            else:
                current.next = Node(value, None)

    # Add nodes to linked list tail
    def append_multi(self, nodes):
        for node in nodes:
            self.append(node)

        return nodes

    # Add a node to a specific position of a linked list
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

    # Add a node before a specific existing node of a linked list
    def insert_before(self, node, new_node):
        new = Node(new_node)

        if self.includes(node) == False:
            return "Node to add before doesn't exist"

        elif self.header.value == node:
            new.next = self.header
            self.header = new

        else:
            current = self.header

            while current != None:
                if current.next.value == node:
                    new.next = current.next
                    current.next = new
                    break

                current = current.next

    # Add a node after a specific existing node of a linked list
    def insert_after(self, node, new_node):
        new = Node(new_node)

        if self.includes(node) == False:
            return "Node to add before doesn't exist"

        else:
            current = self.header

            while current != None:
                if current.value == node:
                    new.next = current.next
                    current.next = new
                    break

                current = current.next

    # Get list length
    def length(self):
        length = 0
        current = self.header

        while current != None:
            length = length + 1
            current = current.next

        return length

    # Return the item at the k order (from tail) of the linked list
    def kth(self, k):
        if k >= self.length() or k < 0:
            raise Exception("Invalid K Input")

        arr = []
        current = self.header

        while current != None:
            arr.append(current.value)
            current = current.next

        result = arr[len(arr) - 1 - k]
        return result

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
