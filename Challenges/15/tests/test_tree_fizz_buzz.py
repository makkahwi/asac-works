import pytest
from tree_fizz_buzz.tree_fizz_buzz import k_ary_tree, fizz_buzz_tree


def test_fizz_buzz(tree):
    actual = fizz_buzz_tree(tree)
    expected = "{ 2 } -> { 1 } -> { Fizz } -> { Buzz } -> { 4 } -> { 6 } -> { 7 } -> { 4 } -> None"
    assert actual == expected


@pytest.fixture
def tree():
    tree = k_ary_tree()
    tree.add_node(2, [1, 3])
    tree.add_node(1, [5, 4])
    tree.add_node(3, [6])
    tree.add_node(5, [7])
    tree.add_node(4)
    return tree
