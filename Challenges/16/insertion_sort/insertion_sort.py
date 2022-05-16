def InsertionSort(arr):
    """
    To insert an array of integers

    Input:
    An array of integeres

    Output:
    Sorted array
    """

    for i in arr:
        if i != int(i):
            raise Exception("Array should have integers only")

    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr


if __name__ == "__main__":
    pass
