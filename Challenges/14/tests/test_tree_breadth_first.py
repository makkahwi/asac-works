import pytest
from tree_breadth_first.tree_breadth_first import (
    BinaryNode,
    BinaryTree,
    BinarySearchTree,
)


def test_contains_true(bst):
    actual = bst.contains(2)
    expected = True
    assert actual == expected


def test_contains_false(bst):
    actual = bst.contains(6)
    expected = False
    assert actual == expected


def test_left_node(bst):
    actual = bst.root.left.value
    expected = 1
    assert actual == expected


def test_right_node(bst):
    actual = bst.root.right.value
    expected = 3
    assert actual == expected


@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.add_node(2)
    bst.add_node(1)
    bst.add_node(3)
    bst.add_node(5)
    bst.add_node(4)
    return bst


def test_preorder(bt):
    actual = bt.type("preorder")
    expected = [1, 3, 5, 4, 2, 7, 6, 8]
    assert actual == expected


def test_inorder(bt):
    actual = bt.type("inorder")
    expected = [5, 3, 4, 1, 7, 2, 6, 8]
    assert actual == expected


def test_postorder(bt):
    actual = bt.type("postorder")
    expected = [5, 3, 4, 7, 2, 6, 8, 1]
    assert actual == expected


@pytest.fixture
def bt():
    bt = BinaryTree()
    bt.root = BinaryNode(1)
    bt.root.right = BinaryNode(2)
    bt.root.left = BinaryNode(3)
    bt.root.left.right = BinaryNode(4)
    bt.root.left.left = BinaryNode(5)
    bt.root.right.right = BinaryNode(6)
    bt.root.right.left = BinaryNode(7)
    bt.root.right.right.right = BinaryNode(8)
    return bt
