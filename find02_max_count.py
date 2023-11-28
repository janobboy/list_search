def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    mx   = data[0]
    while i<len(data):
        x = data[i]

        if x > mx:
            mx = x
        i+=1
    return data.count(mx)
print(find_max_count([1, 8, 3, 8, 5]))
print(find_max_count([13, 8, 3, 4, 9]))
