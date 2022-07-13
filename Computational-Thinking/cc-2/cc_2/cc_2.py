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

    def pop(self):
        if not self.top:
            raise Exception("Empty Stack")

        self.top = self.top.next

    def peek(self):
        if not self.top:
            raise Exception("Empty Stack")

        return self.top.value

    def is_empty(self):
        return not self.top


def validate_brackets(input):
    if input == "":
        raise Exception("Empty input")

    if not isinstance(input, str):
        raise Exception("Input isn't a string")

    stack = Stack()
    new = ""

    for x in input:
        if x == "(" or x == ")" or x == "[" or x == "]" or x == "{" or x == "}":
            new += x

    if new == "":
        raise Exception("No brackets in input")

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

    if stack.is_empty():
        return True

    else:
        return False


if __name__ == "__main__":
    pass
