from cc_2.cc_2 import validate_brackets
import pytest


def test_a_valid():
    actual = validate_brackets("{[()]}")
    expected = True
    assert actual == expected


def test_another_valid():
    actual = validate_brackets("{{[[(())]]}}")
    expected = True
    assert actual == expected


def test_an_invalid():
    actual = validate_brackets("{[(])}")
    expected = False
    assert actual == expected


def test_empty_string():
    with pytest.raises(Exception):
        validate_brackets("")


def test_empty_input():
    with pytest.raises(Exception):
        validate_brackets()


def test_non_string():
    with pytest.raises(Exception):
        validate_brackets(5)


def test_no_brackets_string():
    with pytest.raises(Exception):
        validate_brackets("text")
