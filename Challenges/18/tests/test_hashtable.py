from hashtable.hashtable import Hashtable

import pytest


def test_initializing():
    ht = Hashtable()
    assert ht.size == 100
    assert ht.table == [None] * 100


def test_key_hash():
    ht = Hashtable()
    actual = ht.hash("key1")
    expected = 82
    assert actual == expected


def test_value_set(ht):
    ht.set("key4", "value4")
    actual = ht.get("key4")
    expected = [("key4", "value4")]
    assert actual == expected


def test_key_based_retrieve(ht):
    actual = ht.get("key1")
    expected = [("key1", "value1")]
    assert actual == expected


def test_key_based_retrieve_collision(ht):
    ht.set("key3", "value33")
    actual = ht.get("key3")
    expected = [("key3", "value3"), ("key3", "value33")]
    assert actual == expected


def test_wrong_key_get(ht):
    actual = ht.get("key4")
    expected = None
    assert actual == expected


def test_unique_keys(ht):
    actual = ht.keys()
    expected = ["key2", "key3", "key1"]
    assert actual == expected


def test_contains(ht):
    actual = ht.contains("key1")
    expected = True
    assert actual == expected


def test_contains_wrong(ht):
    actual = ht.contains("key4")
    expected = False
    assert actual == expected


@pytest.fixture
def ht():
    ht = Hashtable()
    ht.set("key3", "value3")
    ht.set("key2", "value2")
    ht.set("key1", "value1")
    return ht
