import pytest
from linked_list.linked_list import linked_list


def test_zip_lists_1(list1, list2):
    actual = linked_list.to_string(linked_list.zip_lists(list1, list2))
    expected = "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> { Node E } -> { Node F } -> None"
    assert actual == expected


def test_zip_lists_2(list1, list3):
    actual = linked_list.to_string(linked_list.zip_lists(list1, list3))
    expected = "{ Node A } -> { Node B } -> { Node C } -> { Node D } -> { Node E } -> { Node F } -> { Node G } -> { Node H } -> None"
    assert actual == expected


@pytest.fixture
def list1():
    list1 = linked_list()
    list1.append("Node A")
    list1.append("Node C")
    list1.append("Node E")
    return list1


@pytest.fixture
def list2():
    list2 = linked_list()
    list2.append("Node B")
    list2.append("Node D")
    list2.append("Node F")
    return list2


@pytest.fixture
def list3():
    list3 = linked_list()
    list3.append("Node B")
    list3.append("Node D")
    list3.append("Node F")
    list3.append("Node G")
    list3.append("Node H")
    return list3
