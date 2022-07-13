import pytest
from stack_and_queue_pseudo.stack_and_queue_pseudo import PseudoQueue


# Can successfully enqueue into a queue
def test_enqueue(queue):
    actual = queue.enqueue("Node D")
    expected = "{ Node D } -> { Node C } -> { Node B } -> { Node A } -> None"
    assert actual == expected


# Can successfully dequeue of a queue
def test_dequeue(queue):
    actual = queue.dequeue()
    expected = "Node A"
    assert actual == expected


# Can's dequeue dequeue of an empty queue
def test_dequeue_empty_list():
    queue = PseudoQueue()
    with pytest.raises(Exception):
        queue().dequeue()


@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue("Node A")
    queue.enqueue("Node B")
    queue.enqueue("Node C")
    return queue
