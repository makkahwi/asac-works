import pytest
from linked_list.linked_list import linked_list


def test_append(list):
    list.append("Node B")
    expected = "{ Node A } -> { Node B } -> None"
    actual = list.to_string()
    assert actual == expected


def test_append_multiple(list):
    new_list = ["Node A", "Node B"]
    expected = new_list
    actual = list.append_multi(new_list)
    assert actual == expected


def test_insert_beofre_middle(list):
    list.append("Node C")
    list.append("Node D")
    list.append("Node E")
    list.append("Node F")
    list.insert_at(int(list.length() / 2) - 1, "Node B")
    expected = "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> { Node E } -> { Node F } -> None"
    actual = list.to_string()
    assert actual == expected


def test_insert_before_header(list):
    list.insert_before(list.header.value, "Node B")
    expected = "{ Node B } -> { Node A } -> None"
    actual = list.to_string()
    assert actual == expected


def test_insert_in_middle(list):
    list.append("Node B")
    list.append("Node D")
    list.append("Node E")
    list.insert_at(int(list.length() / 2), "Node C")
    expected = (
        "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> { Node E } -> None"
    )
    actual = list.to_string()
    assert actual == expected


def test_insert_after_tail(list):
    list.append("Node C")
    list.insert_after("Node A", "Node B")
    expected = "{ Node A } -> { Node B } -> { Node C } -> None"
    actual = list.to_string()
    assert actual == expected


@pytest.fixture
def list():
    list = linked_list()
    list.insert("Node A")
    return list
