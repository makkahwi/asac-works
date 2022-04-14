import pytest
from linked_list.linked_list import linked_list


@pytest.fixture
def list1():
    list1 = linked_list()
    list1.insert("Node A")
    list1.insert("Node C")
    list1.insert("Node E")
    return list1


@pytest.fixture
def list2():
    list2 = linked_list()
    list2.insert("Node B")
    list2.insert("Node D")
    list2.insert("Node F")
    return list2
