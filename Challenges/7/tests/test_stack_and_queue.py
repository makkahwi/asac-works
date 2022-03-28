import pytest
from stack_and_queue.stack_and_queue import Stack, Queue

# Stack Tests #############################################################################

# Can successfully push onto a stack
def test_stack_push(stack):
    actual = stack.push("Node D")
    expected = "{ Node D } -> { Node C } -> { Node B } -> { Node A } -> None"
    assert actual == expected


# Can successfully push multiple values onto a stack
def test_stack_push_multi(stack):
    new = ["Node D", "Node E"]
    actual = stack.push_multi(new)
    expected = (
        "{ Node E } -> { Node D } -> { Node C } -> { Node B } -> { Node A } -> None"
    )
    assert actual == expected


# Can successfully pop off the stack
def test_stack_pop(stack):
    actual = stack.pop()
    expected = "Node C"
    assert actual == expected


# Can successfully empty a stack after multiple pops
def test_stack_pop_all(stack):
    stack.pop_all()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


# Can successfully peek the next item on the stack
def test_stack_peek(stack):
    actual = stack.peek()
    expected = "Node C"
    assert actual == expected


# Can successfully instantiate an empty stack
def test_stack_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


# Calling pop or peek on empty stack raises exception
def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push("Node A")
    stack.push("Node B")
    stack.push("Node C")
    return stack


# Queue Tests #############################################################################

# Can successfully enqueue into a queue
def test_queue_enqueue(queue):
    actual = queue.enqueue("Node D")
    expected = "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> None"
    assert actual == expected


# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multi(queue):
    new = ["Node D", "Node E"]
    actual = queue.enqueue_multi(new)
    expected = (
        "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> { Node E } -> None"
    )
    assert actual == expected


# Can successfully dequeue out of a queue the expected value
def test_queue_dequeue(queue):
    actual = queue.dequeue()
    expected = "Node A"
    assert actual == expected


# Can successfully peek into a queue, seeing the expected value
def test_queue_peek(queue):
    actual = queue.peek()
    expected = "Node A"
    assert actual == expected


# Can successfully empty a queue after multiple dequeues
def test_queue_dequeue_multi(queue):
    queue.dequeue_all()
    actual = queue.is_empty()
    expected = True
    assert actual == expected


# Can successfully instantiate an empty queue
def test_queue_empty():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected


# Calling dequeue or peek on empty queue raises exception
def test_queue_peek_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue("Node A")
    queue.enqueue("Node B")
    queue.enqueue("Node C")
    return queue
