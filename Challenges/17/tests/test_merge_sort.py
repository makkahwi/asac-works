import pytest
from merge_sort.merge_sort import Mergesort


def test_1():
    acutal = Mergesort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert acutal == expected


def test_2():
    acutal = Mergesort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert acutal == expected


def test_3():
    acutal = Mergesort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert acutal == expected


def test_4():
    acutal = Mergesort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert acutal == expected


def test_sort_empty():
    arr = []
    actual = Mergesort(arr)
    expected = None
    assert actual == expected


def test_sort_text():
    arr = [8, 4, 23, 42, 16, 15, "text"]
    with pytest.raises(Exception):
        Mergesort(arr)
