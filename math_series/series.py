def sum_series(n, first=0, second=1):
    result = [first, second]

    i = 2

    while i < n:
        result.append(result[i - 1] + result[i - 2])
        i += 1

    return result[len(result) - 1]


def fibonacci(n):
    return sum_series(n)


def lucas(n):
    return sum_series(n, 2, 1)
