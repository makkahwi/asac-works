from cc_1.cc_1 import super_digit
import pytest


def test_one_digit():
    assert super_digit(8) == 8


def test_two_digits():
    assert super_digit(81) == 9


def test_three_digits():
    assert super_digit(818) == 17


def test_nine_digits():
    assert super_digit(818181818) == 44


def test_negative_input():
    with pytest.raises(Exception):
        assert super_digit(-1)


def test_non_integer_input():
    with pytest.raises(Exception):
        assert super_digit("5")
