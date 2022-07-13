from hashmap_repeated_word.hashmap_repeated_word import repeated_word
import pytest


def test_no_repeat():
    acutal = repeated_word("hello world war three")
    expected = "No Repeated Words"
    assert acutal == expected


def test_repeated_word():
    acutal = repeated_word("hello to the world of world war three")
    expected = "world"
    assert acutal == expected


def test_non_string():
    with pytest.raises(Exception):
        repeated_word(9)


def test_empty_string():
    with pytest.raises(Exception):
        repeated_word("")
