def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    minNum = []
    x = 0
    
    while x < len(data):
        if data[x]%2==0:
            minNum.append(data[x])
        x += 1
    a = min(minNum)
        
    return minNum, a
print(find_min_even([1, 8, 2, 8, 5]))
