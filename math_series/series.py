def sum_series(n, first=0, second=1):
    """
    To sum the series, either as a fibonacci or lucas and return nth value

    Input
    nth item to return, optional first & second elements of the series

    Output
    value of the series @ position of n
    """

    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first=first, second=second) + sum_series(
            n - 2, first=first, second=second
        )


def fibonacci(n):
    """
    To return the nth elemnts of fibonacci series (which starts with 0 & 1)

    Input
    nth item to return

    Output
    value of the series @ position of n
    """

    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    To return the nth elemnts of lucas series (which starts with 2 & 1)

    Input
    nth item to return

    Output
    value of the series @ position of n
    """

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
