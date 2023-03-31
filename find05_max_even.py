def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    x = 0
    maxNum = []
    while x < len(data):
        if data[x]%2 == 0:
            maxNum.append(data[x])
        x += 1
    maxNum = max(maxNum)
    return maxNum

print(find_max_even( [1, 4,11, 3, 8, 5]))