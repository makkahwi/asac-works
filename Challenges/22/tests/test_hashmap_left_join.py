import pytest
from hashmap_left_join.hashmap_left_join import left_join, Hashtable


def test_join(ht1, ht2):
    ht3 = left_join(ht1, ht2)

    actual = ht3.get("key2")
    expected = [("key2", ["value2-1", "value2-2"])]
    assert actual == expected


def test_join_empty(ht1):
    ht2 = Hashtable()
    ht3 = left_join(ht1, ht2)

    actual = ht3.get("key1")
    expected = [("key1", ["value1-1"])]
    assert actual == expected


def test_join_emptys():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht3 = left_join(ht1, ht2)

    actual = ht3.keys()
    expected = []
    assert actual == expected


@pytest.fixture
def ht1():
    ht1 = Hashtable()
    ht1.set("key3", "value3-1")
    ht1.set("key2", "value2-1")
    ht1.set("key1", "value1-1")
    return ht1


@pytest.fixture
def ht2():
    ht2 = Hashtable()
    ht2.set("key3", "value3-2")
    ht2.set("key2", "value2-2")
    ht2.set("key1", "value1-2")
    return ht2
