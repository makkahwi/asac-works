import pytest
from quick_sort.quick_sort import QuickSort


def test_sort_1():
    acutal = QuickSort([8, 4, 23, 42, 16, 15], 0, 5)
    expected = [4, 8, 15, 16, 23, 42]
    assert acutal == expected


def test_sort_2():
    acutal = QuickSort([20, 18, 12, 8, 5, -2], 0, 5)
    expected = [-2, 5, 8, 12, 18, 20]
    assert acutal == expected


def test_sort_3():
    acutal = QuickSort([5, 12, 7, 5, 5, 7], 0, 5)
    expected = [5, 5, 5, 7, 7, 12]
    assert acutal == expected


def test_sort_4():
    acutal = QuickSort([2, 3, 5, 7, 13, 11], 0, 5)
    expected = [2, 3, 5, 7, 11, 13]
    assert acutal == expected


def test_sort_empty():
    with pytest.raises(Exception):
        QuickSort([], 0, 4)


def test_sort_non_list():
    with pytest.raises(Exception):
        QuickSort(9, 0, 4)


def test_sort_non_integer_list():
    with pytest.raises(Exception):
        QuickSort([9, "9"], 0, 4)
