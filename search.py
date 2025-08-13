def linear_search_1(lst: list, item: int) -> int:
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

def linear_search_2(lst: list, item: int) -> int:
    i = 0
    while i <= len(lst) - 1:
        if lst[i] == item:
            return i
        i += 1

    return -1

def binary_search(lst: list, item: int) -> int:
    i = 0
    j = m = len(lst) - 1
    while i <= j:
        m = m//2
        if lst[m] > item:
            j = m - 1
        elif lst[m] < item:
            i = m + 1
        else:
            return m

    return -1