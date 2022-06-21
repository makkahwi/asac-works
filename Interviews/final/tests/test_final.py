from final.final import tree_mirroring, BinaryNode, BinaryTree
import pytest


def test_empty_tree():
    bt = BinaryTree()

    with pytest.raises(Exception):
        tree_mirroring(bt)


def test_root_only():
    bt = BinaryTree()
    bt.root = BinaryNode(5)
    assert tree_mirroring(bt) == bt


def test_mirroring(bt1, bt2):
    actual = tree_mirroring(bt1)
    expected = bt2
    assert actual == expected


@pytest.fixture
def bt1():
    bt1 = BinaryTree()
    bt1.root = BinaryNode(5)
    bt1.root.left = BinaryNode(6)
    bt1.root.left.left = BinaryNode(1)
    bt1.root.left.right = BinaryNode(2)
    bt1.root.right = BinaryNode(7)
    bt1.root.right.left = BinaryNode(3)
    bt1.root.right.right = BinaryNode(4)
    return bt1


@pytest.fixture
def bt2():
    bt2 = BinaryTree()
    bt2.root = BinaryNode(5)
    bt2.root.left = BinaryNode(7)
    bt2.root.left.left = BinaryNode(4)
    bt2.root.left.right = BinaryNode(3)
    bt2.root.right = BinaryNode(6)
    bt2.root.right.left = BinaryNode(2)
    bt2.root.right.right = BinaryNode(1)
    return bt2
