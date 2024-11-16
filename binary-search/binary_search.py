def find(search_list, value):
    sorted_list = search_list.sort()
    if len(search_list) == 0:
        raise ValueError("value not in array")
    
    i = 0
    j = len(search_list) - 1
    while i <= j:
        mid = (i + j) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            i = mid + 1
        else:
            j = mid - 1
    raise ValueError("value not in array")
