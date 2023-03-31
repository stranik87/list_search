def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    x = 0
    max1 = 0
    min1 = 0
    while x < len(data):
        if max1 < data[x]:
            max1 = data[x]
        min1 = min(data) 
        
        x += 1
    return max1 + min1
print(find_max_min_sum([1, 2, 3, 4, 5]))
