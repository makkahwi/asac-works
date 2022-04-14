import pytest
from stack_and_queue_pseudo.stack_and_queue_pseudo import PseudoQueue

# Can successfully enqueue into a queue
def test_enqueue(queue):
    actual = queue.enqueue("Node D")
    expected = "Node D"
    assert actual == expected


# Can successfully dequeue out of a queue the expected value
def test_dequeue(queue):
    actual = queue.dequeue()
    expected = "Node C"
    assert actual == expected


@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue("Node A")
    queue.enqueue("Node B")
    queue.enqueue("Node C")
    return queue
