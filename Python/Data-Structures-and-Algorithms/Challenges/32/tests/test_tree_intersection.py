import pytest
from tree_intersection.tree_intersection import (
    BinaryNode,
    BinaryTree,
    tree_intersection,
)


def test_two_trees_no_common(bt1, bt3):
    actual = tree_intersection(bt1, bt3)
    expected = []
    assert actual == expected


def test_two_trees_with_common(bt1, bt2):
    actual = tree_intersection(bt1, bt2)
    expected = [4, 2, 6, 8]
    assert actual == expected


def test_an_empty_tree(bt1):
    bt2 = BinaryTree()

    with pytest.raises(Exception):
        tree_intersection(bt1, bt2)


def test_empty_trees():
    bt1 = BinaryTree()
    bt2 = BinaryTree()

    with pytest.raises(Exception):
        tree_intersection(bt1, bt2)


def test_an_non_tree(bt1):
    with pytest.raises(Exception):
        tree_intersection(bt1, 5)


def test_non_trees():
    with pytest.raises(Exception):
        tree_intersection("bt", 9)


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


@pytest.fixture
def bt3():
    bt3 = BinaryTree()
    bt3.root = BinaryNode(12)
    bt3.root.right = BinaryNode(9)
    bt3.root.left = BinaryNode(11)
    bt3.root.left.right = BinaryNode(9)
    bt3.root.left.left = BinaryNode(10)
    bt3.root.right.right = BinaryNode(9)
    bt3.root.right.left = BinaryNode(9)
    bt3.root.right.right.right = BinaryNode(11)
    return bt3
