import pytest
from tree_max.tree_max import BinaryNode, BinaryTree, BinarySearchTree


def test_tree_max(bt):
    acutal = bt.tree_max()
    expected = 8
    assert acutal == expected


def test_empty_tree_max():
    bt = BinaryTree()
    with pytest.raises(Exception):
        bt().tree_max()


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
