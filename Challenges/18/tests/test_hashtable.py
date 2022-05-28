from hashtable.hashtable import Hashtable

import pytest


def test_value_set(ht):
    actual = ht.set("key4", "value4")
    expected = [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
        ("key4", "value4"),
    ]
    assert actual == expected


def test_key_based_retrieve(ht):
    actual = ht.get("key1")
    expected = "value1"
    assert actual == expected


def test_wrong_key_get(ht):
    actual = ht.get("key4")
    expected = None
    assert actual == expected


def test_unique_keys(ht):
    actual = ht.keys()
    expected = ["key1", "key2", "key3"]
    assert actual == expected


def test_collision_handle():
    pass


def test_value_with_collision():
    pass


def test_key_hash():
    ht = Hashtable()
    actual = ht.hash("key1", "value1")
    expected = "value1"
    assert actual == expected


@pytest.fixture
def ht():
    ht = Hashtable()
    ht.set("key3", "value3")
    ht.set("key2", "value2")
    ht.set("key1", "value1")
    return ht
