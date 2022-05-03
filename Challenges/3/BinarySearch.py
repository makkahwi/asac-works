from ast import Num


def BinarySearch(arr, key):

    if not isinstance(arr, list) or arr.length == 0:
        return "First Input should be a non-empty array"

    if not isinstance(key, Num):
        return "Second Input should be a number"

    answer = -1
    middle = 0

    if arr.length % 2 == 0:
        middle = arr.length / 2

    else:
        middle = int(arr.length / 2) + 1

    start = 0
    end = arr.length - 1

    while end - start > 2:

        if arr[middle] == key:
            answer = middle
            break

        if arr[middle] > key:
            end = int(middle)

            if int(middle / 2) % 2 == 0:
                middle = int(middle / 2)
            else:
                middle = int(middle / 2) + 1

        else:
            start = int(middle)

            if int(middle * 1.5) % 2 == 0:
                middle = int(middle * 1.5)
            else:
                middle = int(middle * 1.5) + 1

    return answer
