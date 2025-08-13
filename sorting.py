from typing import Optional


def selection_sort(lst: list) -> None:
    for i in range(len(lst)):
        # simple: min_index = min(min(s[i:]), s[i])
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]


def insertion_sort(lst: list) -> None:
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1


def bubble_sort(lst: list) -> None:
    for j in range(1, len(lst)):
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]


def bubble_sort_2(lst: list) -> None:  # Faster than regular bubble sort
    not_done = True
    while not_done:
        not_done = False
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                not_done = True
                lst[i], lst[i - 1] = lst[i - 1], lst[i]


def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    left = merge_sort(lst[:len(lst) // 2])
    right = merge_sort(lst[len(lst) // 2:])


def mergesort2(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    left = mergesort2(lst[:len(lst) // 2])
    right = mergesort2(lst[len(lst) // 2:])

    return merge2(left, right)


def merge2(lst1: list, lst2: list) -> list:
    l, r = 0, 0
    sorted_arr = []

    while l < len(lst1) and r < len(lst2):
        if lst1[l] < lst2[r]:
            sorted_arr.append(lst1[l])
            l += 1
        else:
            sorted_arr.append(lst2[r])
            r += 1

    return sorted_arr + lst2[l:] + lst1[r:]


def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst[:]
    else:
        pivot = lst[-1]
        left = [x for x in lst[:-1] if x <= pivot]
        right = [x for x in lst[:-1] if x > pivot]
        left = quick_sort(left)
        right = quick_sort(right)

        return left + [pivot] + right


def inplace_quick_sort(lst: list, start: Optional[int] = None, end: Optional[int] = None) -> list:
    if start is None: start = 0
    if end is None: end = len(lst) - 1

    if start < end:
        pivot = lst[start]
        s = start + 1

        for i in range(start, end):
            if lst[i] < pivot:
                lst[i], lst[s] = lst[s], lst[i]
                s+=1

        lst[start], lst[s-1] = lst[start], lst[s-1]
        p = s - 1
        inplace_quick_sort(lst, start, p-1)
        inplace_quick_sort(lst, p+1, end)


def counting_sort(lst: list) -> None:
    # this implementation only works for positive numbers
    # counting sort can work for negative numbers
    max_num = max(lst)
    counts = [0] * (max_num + 1)
    for num in lst:
        counts[num] += 1
    i = 0
    for c in range(max_num + 1):
        while counts[c] > 0:
            lst[i] = c
            i += 1
            counts[c] -= 1