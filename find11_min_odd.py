def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    minNum = []
    x = 0
    
    while x < len(data):
        if data[x]%2 == 1:
            minNum.append(data[x])
        x += 1
    a = min(minNum)
    return minNum, a

print(find_min_odd([7, 8, 4, 3, 5]))

