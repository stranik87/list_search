def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    x = 0 
    max1 = 0
    cnt = 0
    while x < len(data):
        if max1 < data[x]:
            max1 = data[x]
        cnt = data.count(max1)        
        x += 1
    return cnt

print(find_max_count([1, 8, 3, 8, 5]))
