import pytest
from trees.trees import BinaryNode, BinaryTree, BinarySearchTree


# 1. Can successfully instantiate an empty tree
def test_initiate_empty_bst():
    bst = BinarySearchTree()

    with pytest.raises(Exception):
        bst.contains(2)


# 2. Can successfully instantiate a tree with a single root node
def test_initiate_bst_root():
    bst = BinarySearchTree()
    bst.root = BinaryNode(2)
    actual = bst.contains(2)
    expected = True
    assert actual == expected


# 3. For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_bst_root_children():
    bst = BinarySearchTree()
    bst.root = BinaryNode(2)
    bst.add_node(1)
    bst.add_node(3)
    actual1 = bst.root.left.value
    expected1 = 1
    actual2 = bst.root.right.value
    expected2 = 3
    assert actual1 == expected1
    assert actual2 == expected2


# 4. Can successfully return a collection from a preorder traversal
def test_preorder(bt):
    actual = bt.type("preorder")
    expected = [1, 3, 5, 4, 2, 7, 6, 8]
    assert actual == expected


# 5. Can successfully return a collection from an inorder traversal
def test_inorder(bt):
    actual = bt.type("inorder")
    expected = [5, 3, 4, 1, 7, 2, 6, 8]
    assert actual == expected


# 6. Can successfully return a collection from a postorder traversal
def test_postorder(bt):
    actual = bt.type("postorder")
    expected = [5, 3, 4, 7, 2, 6, 8, 1]
    assert actual == expected


# 7. Returns true or false for the contains method, given an existing or non-existing node value
def test_contains_true(bst):
    actual = bst.contains(2)
    expected = True
    assert actual == expected


# 7. Returns true or false for the contains method, given an existing or non-existing node value
def test_contains_false(bst):
    actual = bst.contains(6)
    expected = False
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
