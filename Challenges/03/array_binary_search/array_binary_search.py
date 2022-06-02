from ast import Num


def assignMiddle(length):
    # arr length is even
    if length % 2 == 0:
        middle = int(length / 2)

    # arr length is odd
    else:
        middle = int(length / 2) + 1

    return middle


def BinarySearch(arr, key):

    # Check First Input Type
    if not isinstance(arr, list) or len(arr) == 0:
        return "First Input should be a non-empty array"

    # Check Second Input Type
    if not isinstance(key, int):
        return "Second Input should be a number"

    answer = -1

    # Define the index of middle item of arr
    middle = assignMiddle(len(arr))

    # Search Range
    start = 0
    end = len(arr) - 1

    while end - start > 2:

        # When required key is found
        if arr[middle] == key:
            answer = middle
            break

        # When required key is bigger than the current middle index of current search range
        if arr[middle] > key:
            # Update search range
            end = int(middle)

            # Update middle index
            middle = assignMiddle(int(middle / 2))

        # When required key is smaller than the current middle index of current search range
        else:
            # Update search range
            start = int(middle)

            # Update middle index
            middle = assignMiddle(int(middle * 1.5))

    return answer
