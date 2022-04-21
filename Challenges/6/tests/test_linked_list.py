import pytest
from linked_list.linked_list import linked_list


def test_greater_than_length(list):
    with pytest.raises(Exception):
        list.kth(5)


def test_equal_length(list):
    with pytest.raises(Exception):
        list.kth(5)


def test_negative(list):
    with pytest.raises(Exception):
        list.kth(-9)


def test_size_one_list(list):
    actual = "Node A"
    expected = list.kth(0)
    assert actual == expected


def test_happy_path(list):
    list.append("Node B")
    actual = "Node A"
    expected = list.kth(1)
    assert actual == expected


@pytest.fixture
def list():
    list = linked_list()
    list.insert("Node A")
    return list
