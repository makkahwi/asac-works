import pytest
from tree_intersection.tree_intersection import (
    BinaryNode,
    BinaryTree,
    tree_intersection,
)


def test_two_trees(bt1, bt2):
    actual = tree_intersection(bt1, bt2)
    expected = [4, 2, 6, 8]
    assert actual == expected


def test_an_empty_tree(bt1):
    bt2 = BinaryTree()

    actual = tree_intersection(bt1, bt2)
    expected = []
    assert actual == expected


@pytest.fixture
def bt1():
    bt1 = BinaryTree()
    bt1.root = BinaryNode(1)
    bt1.root.right = BinaryNode(2)
    bt1.root.left = BinaryNode(3)
    bt1.root.left.right = BinaryNode(4)
    bt1.root.left.left = BinaryNode(5)
    bt1.root.right.right = BinaryNode(6)
    bt1.root.right.left = BinaryNode(7)
    bt1.root.right.right.right = BinaryNode(8)
    return bt1


@pytest.fixture
def bt2():
    bt2 = BinaryTree()
    bt2.root = BinaryNode(12)
    bt2.root.right = BinaryNode(2)
    bt2.root.left = BinaryNode(11)
    bt2.root.left.right = BinaryNode(4)
    bt2.root.left.left = BinaryNode(10)
    bt2.root.right.right = BinaryNode(6)
    bt2.root.right.left = BinaryNode(9)
    bt2.root.right.right.right = BinaryNode(8)
    return bt2
