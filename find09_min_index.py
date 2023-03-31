def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    minNum = min(data)
    x = data.index(minNum)
    return minNum, x

print(find_min_index([1, 2, -3, 4, 5]))

