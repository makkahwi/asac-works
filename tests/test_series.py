from math_series.series import fibonacci, lucas


def test_tweleve():
    actual = fibonacci(12)
    expected = 89
    assert actual == expected


def test_ten():
    actual = lucas(10)
    expected = 76
    assert actual == expected
