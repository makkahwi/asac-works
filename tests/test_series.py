from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_twenty():
    actual = lucas(20)
    expected = 15127
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_sum_series_fibonacci_20():
    actual = sum_series(20)
    expected = 6765
    assert actual == expected


def test_sum_series_lucas_20():
    actual = sum_series(20, 2, 1)
    expected = 15127
    assert actual == expected
