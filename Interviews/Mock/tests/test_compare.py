from compare.compare import compare_trees, BinaryNode, BinaryTree
import pytest


def test_1(bt1):
    actual = compare_trees(bt1, bt1)
    expected = True
    assert actual == expected


def test_2(bt1, bt2):
    actual = compare_trees(bt1, bt2)
    expected = False
    assert actual == expected


def test_3(bt2):
    actual = compare_trees(bt2, bt2)
    expected = True
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
    bt2.root = BinaryNode(1)
    bt2.root.right = BinaryNode(2)
    bt2.root.left = BinaryNode(3)
    bt2.root.left.right = BinaryNode(4)
    bt2.root.left.left = BinaryNode(5)
    bt2.root.right.right = BinaryNode(6)
    bt2.root.right.left = BinaryNode(9)
    bt2.root.right.right.right = BinaryNode(8)
    return bt2
