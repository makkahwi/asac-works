from array_binary_search.array_binary_search import BinarySearch


def test_1():
    arr = [4, 8, 15, 16, 23, 42]
    key = 15
    acutal = BinarySearch(arr, key)
    expected = 2
    assert acutal == expected


def test_2():
    arr = [-131, -82, 0, 27, 42, 68, 179]
    key = 42
    acutal = BinarySearch(arr, key)
    expected = 4
    assert acutal == expected


def test_3():
    arr = [11, 22, 33, 44, 55, 66, 77]
    key = 90
    acutal = BinarySearch(arr, key)
    expected = -1
    assert acutal == expected


def test_4():
    arr = [1, 2, 3, 5, 6, 7]
    key = 4
    acutal = BinarySearch(arr, key)
    expected = -1
    assert acutal == expected
