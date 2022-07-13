from second.second import checkLinkedList, linked_list
import pytest


def test_1(list1):
    actual = checkLinkedList(list1)
    expected = False
    assert actual == expected


def test_2(list2):
    actual = checkLinkedList(list2)
    expected = True
    assert actual == expected


@pytest.fixture
def list1():
    list1 = linked_list()
    list1.insert("A")
    list1.insert("B")
    list1.insert("C")
    return list1


@pytest.fixture
def list2():
    list2 = linked_list()
    list2.insert("A")
    list2.insert("B")
    list2.insert("A")
    return list2
