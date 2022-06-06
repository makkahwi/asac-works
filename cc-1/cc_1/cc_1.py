from logging import exception


def super_digit(num):
    if not isinstance(num, int) or num < 0:
        raise Exception("Input should be a non-negative integer")

    if num < 10:
        return num

    else:
        return num % 10 + super_digit(int(num / 10))
