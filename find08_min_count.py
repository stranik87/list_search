def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    x = min(data)
    a = data.count(x)
    return x , a

print(find_min_count([0, -4, 3, 9, -2, -4]))
