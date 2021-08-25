import random

input_array = list(random.choices(range(-100, 100), k=25))


def start():
    print('1). Arrays algorithms')
    print('Input array:')
    print(input_array)
    print('Selection sort:')
    output_array_1 = selection_sort(input_array)
    print(output_array_1)
    print('Selection sort recursive:')
    output_array_2 = selection_sort_recursive(input_array)
    print(output_array_2)
    print('Bubble sort:')
    output_array_3 = bubble_sort(input_array)
    print(output_array_3)


# selection sort
def selection_sort(array):
    # loop through array
    for i in range(len(array)):
        # init min index as first index
        min_index = i
        # find index of min value in rest array
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # if new min index, then swap elements
        if min_index > i:
            array[min_index], array[i] = array[i], array[min_index]
    return array


# selection sort with recursion
def selection_sort_recursive(array, first_index=0):
    # init min index as first index
    min_index = first_index
    # find index of min value in array
    for i in range(first_index, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    # if new min index, then swap elements
    if min_index > first_index:
        array[min_index], array[first_index] = array[first_index], array[min_index]
    # call a recursion with next first index till penultimate index
    if first_index < len(array) - 2:
        array = selection_sort_recursive(array, first_index + 1)
    return array


#bubble sort
def bubble_sort(array):
    # loop through array
    for i in range(len(array)):
        try:
            # next index
            j = i + 1
            # if current value > next value, swap elements
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        except IndexError:
            # if next list index does not exists -> end of list, return
            return array