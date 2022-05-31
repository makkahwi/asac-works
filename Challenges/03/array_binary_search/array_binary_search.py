from ast import Num


def BinarySearch(arr, key):

    # Check First Input Type
    if not isinstance(arr, list) or arr.length == 0:
        return "First Input should be a non-empty array"

    # Check Second Input Type
    if not isinstance(key, Num):
        return "Second Input should be a number"

    answer = -1
    middle = 0

    # Define the index of middle item of arr
    # arr length is even
    if arr.length % 2 == 0:
        middle = arr.length / 2

    # arr length is odd
    else:
        middle = int(arr.length / 2) + 1

    # Search Range
    start = 0
    end = arr.length - 1

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
            if int(middle / 2) % 2 == 0:
                middle = int(middle / 2)
            else:
                middle = int(middle / 2) + 1

        # When required key is smaller than the current middle index of current search range
        else:
            # Update search range
            start = int(middle)

            # Update middle index
            if int(middle * 1.5) % 2 == 0:
                middle = int(middle * 1.5)
            else:
                middle = int(middle * 1.5) + 1

    return answer
