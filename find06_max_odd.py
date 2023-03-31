def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    x = 0
    a = 0
    maxOdd = -1
    maxNum = [] 
    while x < len(data):
        if data[x]%2 == 1:
            maxNum.append(data[x])
            a = max(maxNum)
        elif a%2 != 1:
            return -1
        x += 1
    return maxNum ,a

print(find_max_odd([1, 8, 3, 8, 5]))