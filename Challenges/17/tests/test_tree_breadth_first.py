import pytest
from tree_breadth_first.tree_breadth_first import BinarySearchTree, breadth_first


def test_breadth_first(bst):
    actual = breadth_first(bst)
    expected = [2, 1, 3, 5, 4]
    assert actual == expected


def test_empty_breadth_first():
    bst = BinarySearchTree()

    with pytest.raises(Exception):
        breadth_first(bst)


@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.add_node(2)
    bst.add_node(1)
    bst.add_node(3)
    bst.add_node(5)
    bst.add_node(4)
    return bst
