def sumOfMatrix(matrix):
    result = []

    for array in matrix:
        sum = 0
        for no in array:
            sum += no
        result.append(sum)

    return result
