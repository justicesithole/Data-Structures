#Python Sorting Functions Algorithm
import time
#Buble Sort

def bubble_sort(my_list):
    start = time.time()
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) - 1 -i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    end = time.time()
    
    return my_list, end-start

#Insertion sort
def insertion_sort(my_list):
    start = time.time()
    for i in range(1, len(my_list)):
        cur_num = my_list[i]
        for j in range(i - 1, 0, -1):
            if my_list[j] > cur_num:
                my_list[j + 1] = my_list[j]
            else:
                my_list[j + 1] = cur_num
                break
    end = time.time()
    return my_list, end-start

#merge sort
def merge_sort(my_list):
    start = time.time()
    merge_sort2(my_list, 0, len(my_list) - 1)
    end = time.time()
    return my_list, end-start

def merge_sort2(my_list, first, last):
    the_list = None
    if first < last:
        middle = (first + last) // 2
        merge_sort2(my_list, first, middle)
        merge_sort2(my_list, middle + 1, last)
        merge(my_list, first, middle, last)
        

def merge(my_list, first, middle, last):
    L = my_list[first:middle]
    R = my_list[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            my_list[k] = L[i]
            i += 1
        else:
            my_list[k] = R[j]
            j += 1

#Quick sort 
def quick_sort(my_list):
    start = time.time()
    quick_sort2(my_list, 0, len(my_list) - 1)
    end = time.time()
    return my_list, end-start

def quick_sort2(my_list, low, hi):
    if low < hi:
        p = partition(my_list, low, hi)
        quick_sort2(my_list, low, p - 1)
        quick_sort2(my_list, p + 1, hi)

def get_pivot(my_list, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if my_list[low] < my_list[mid]:
        if my_list[mid] < my_list[hi]:
            pivot = mid
    elif my_list[low] < my_list[hi]:
        pivot = low
    return pivot

def partition(my_list, low, hi):
    pivot_index = get_pivot(my_list, low, hi)
    pivot_value = my_list[pivot_index]
    my_list[pivot_index], my_list[low] = my_list[low], my_list[pivot_index]
    border = low

    for i in range(low, hi + 1):
        if my_list[i] < pivot_value:
            border += 1
            my_list[i], my_list[border] = my_list[border], my_list[i]
    my_list[low], my_list[border] = my_list[border], my_list[low]

    return (border)

#Selection sort

def selection_sort(my_list):
    start = time.time()
    for i in range(0, len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list, my_list[min_index] = my_list[min_index], my_list[i]
    end = time.time()
    return my_list, end-start
            
