from sort_module import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
import random
import time

the_list = []
for i in range(10000):
    the_list.insert(0, i)

list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []

def list_sort(the_list):
    start = time.time()
    a_list = the_list.sort()
    end = time.time()
    return end-start
a, bubble_time = bubble_sort(the_list)
b, insertion_time = insertion_sort(the_list)
c, merge_time = merge_sort(the_list)
d, quick_time = quick_sort(the_list)
e, selection_time = selection_sort(the_list)

list_1.append(bubble_time)
list_2.append(insertion_time)
list_3.append(merge_time)
list_4.append(quick_time)
list_5.append(selection_time)
list_6.append(list_sort(the_list))    

print("Sorting using python\t", list_6)
print()
print("Bubble sort time\t", list_1)
print()
print("Insertion sort time\t", list_2)
print()
print("Merge sort time\t\t", list_3)
print()
print("Quick sort time\t\t", list_4)
print()
print("Selection sort time\t", list_5)
input("Press enter to exit:")
