import pytest
from stack_and_queue_brackets.stack_and_queue_brackets import validate_brackets


def test_a_valid():
    actual = validate_brackets("[text]")
    expected = True
    assert actual == expected


def test_another_valid():
    actual = validate_brackets("(1)[2](3)")
    expected = True
    assert actual == expected


def test_an_invalid():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected


def test_another_invalid():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected


def test_null():
    with pytest.raises(Exception):
        validate_brackets(None)


def test_no_brackets():
    with pytest.raises(Exception):
        validate_brackets("text")
