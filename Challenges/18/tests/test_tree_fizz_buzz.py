from unittest.case import _AssertRaisesContext
from attr import asdict
import pytest
from tree_fizz_buzz.tree_fizz_buzz import tree_node, k_ary_tree, fizz_buzz_tree


def test_fizz_buzz(tree):
    actual = fizz_buzz_tree(tree).breadth_first()
    expected = [
        "7",
        "Fizz",
        "Buzz",
        "7",
        "1",
        "Fizz",
        "8",
        "FizzBuzz",
        "Fizz",
        "4",
        "Fizz",
        "Fizz",
        "Buzz",
    ]
    assert actual == expected


def test_empty_tree():
    tree = k_ary_tree()
    with pytest.raises(Exception):
        fizz_buzz_tree(tree)


def test_no_children_tree():
    root = tree_node(5)
    tree = k_ary_tree(root)

    actual = fizz_buzz_tree(tree).breadth_first()
    expected = ["Buzz"]
    assert actual == expected


@pytest.fixture
def tree():
    t1 = tree_node(1)
    t2 = tree_node(3)
    t3 = tree_node(9)
    t4 = tree_node(4)
    t5 = tree_node(8)
    t6 = tree_node(15)
    t7 = tree_node(54)
    t8 = tree_node(9)
    t88 = tree_node(5)
    t9 = tree_node(12, [t1, t2, t5, t6])
    t10 = tree_node(5, [t3, t4, t7])
    t11 = tree_node(7, [t8, t88])
    t12 = tree_node(7, [t9, t10, t11])
    tree = k_ary_tree(t12)
    return tree


# Tree Structure
#                                       ---
#                                      | 7 |
#                                       ---

#        ----                                  ---                       ---
#       | 12 |                                | 5 |                     | 7 |
#        ----                                  ---                       ---

#  ---    ---    ---    ----            ---    ---    ----            ---    ---
# | 1 |  | 3 |  | 8 |  | 15 |          | 9 |  | 4 |  | 54 |          | 9 |  | 5 |
#  ---    ---    ---    ----            ---    ---    ----            ---    ---
