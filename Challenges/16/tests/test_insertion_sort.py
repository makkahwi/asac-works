from insertion_sort.insertion_sort import InsertionSort
import pytest


def test_sort():
    arr = [8, 4, 23, 42, 16, 15]
    actual = InsertionSort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_sort_reverse():
    arr = [20, 18, 12, 8, 5, -2]
    actual = InsertionSort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_sort_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    actual = InsertionSort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_sort_nearly():
    arr = [2, 3, 5, 7, 13, 11]
    actual = InsertionSort(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_sort_empty():
    arr = []
    actual = InsertionSort(arr)
    expected = []
    assert actual == expected


def test_sort_text():
    arr = [8, 4, 23, 42, 16, 15, "text"]
    with pytest.raises(Exception):
        InsertionSort(arr)
