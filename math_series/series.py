def sum_series(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first=first, second=second) + sum_series(
            n - 2, first=first, second=second
        )


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
