import pytest
from linked_list.linked_list import linked_list


def test_empty_list():
    list = linked_list()
    expected = "List exists but has no nodes"
    actual = list.to_string()
    assert actual == expected


def test_insert_to_list(list):
    expected = "{ Node A } -> None"
    actual = list.to_string()
    assert actual == expected


def test_header_of_empty_list():
    list = linked_list()
    expected = None
    actual = list.header
    assert actual == expected


def test_insert_multiple(list):
    new_list = ["Node A", "Node B"]
    expected = new_list
    actual = list.insert_multi(new_list)
    assert actual == expected


def test_value1_existence_in_list(list):
    list.insert("Node A")
    expected = True
    actual = list.includes("Node A")
    assert actual == expected


def test_value2_existence_in_list(list):
    list.insert("Node A")
    expected = False
    actual = list.includes("Node C")
    assert actual == expected


def test_return_list(list):
    expected = "{ Node A } -> None"
    actual = list.to_string()
    assert actual == expected


@pytest.fixture
def list():
    list = linked_list()
    list.insert("Node A")
    return list
