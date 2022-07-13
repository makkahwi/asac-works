from cc_3.cc_3 import fibonacci
import pytest


def test_zero():
    with pytest.raises(Exception):
        fibonacci(0)


def test_negative():
    with pytest.raises(Exception):
        fibonacci(-5)


def test_non_integer():
    with pytest.raises(Exception):
        fibonacci("0")


def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_ninty_nine():
    actual = fibonacci(99)
    expected = 196418
    assert actual == expected
