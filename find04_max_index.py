def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    
    maxNum = max(data)
    x = data.index(maxNum)
    return x

print(find_max_index([1, 2, 3, 4, 5]))
