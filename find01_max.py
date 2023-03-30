def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max1 = 0
    x = 0
    while x < len(data):
        if max1 < data[x]:
            max1 = data[x]
        x += 1
    
    return max1
print(find_max([1, 2, 3, 4, 5]))
    