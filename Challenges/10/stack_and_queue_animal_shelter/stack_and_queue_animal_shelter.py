class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


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


class Cat:
    def __init__(self):
        self.type = "cat"


class Dog:
    def __init__(self):
        self.type = "dog"


class Hamster:
    def __init__(self):
        pass


class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            self.shelter.enqueue(animal)
        else:
            raise Exception("Shelter can have cats or dogs only")

        return self.to_string()

    def dequeue(self, pref):
        if self.shelter == None:
            raise Exception("Empty Shelter")

        elif pref.lower() != "cat" or pref.lower() != "dog":
            raise Exception("Shelter only contains cats and cogs")

        else:
            current = self.shelter.front
            temp = self.shelter.front
            tempNext = temp.next

            while temp != None and tempNext != None:
                if str(temp.value) != pref:
                    temp = temp.next
                    tempNext = tempNext.next

                elif str(temp.value) == pref:
                    currentV = current.value
                    self.shelter.front.value = temp.value
                    temp.value = currentV
                    tempNext = tempNext.next
                    self.shelter.dequeue()
                    return str(current.value)
            else:
                raise Exception("Animal isn't in the shelter")

        return self.to_string()

    def to_string(self):
        queue_str = ""
        if self.shelter.front == None:
            queue_str = "Shelter is empty"
        else:
            current = self.shelter.front
            while current:
                queue_str += "{ " + str(current.value) + " }" + " -> "
                current = current.next
            queue_str += "None"
        return queue_str


if __name__ == "__main__":
    pass
