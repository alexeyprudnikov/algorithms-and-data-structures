import random

# generate random list from -100 to 100 of 25 elements
input_list = list(random.choices(range(-100, 100), k=25))


def start():
    print('1). Lists algorithms')
    print('Input list:')
    print(input_list)
    print('Selection sort:')
    output_list = selection_sort(input_list)
    print(output_list)
    print('Selection sort recursive:')
    output_list = selection_sort_recursive(input_list)
    print(output_list)
    print('Bubble sort:')
    output_list = bubble_sort(input_list)
    print(output_list)


# selection sort
def selection_sort(list):
    # loop through list
    for i in range(len(list)):
        # init min index as first index
        min_index = i
        # find index of min value in rest list
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        # if new min index, then swap elements
        if min_index > i:
            list[min_index], list[i] = list[i], list[min_index]
    return list


# selection sort with recursion
def selection_sort_recursive(list, first_index=0):
    # init min index as first index
    min_index = first_index
    # find index of min value in list
    for i in range(first_index, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    # if new min index, then swap elements
    if min_index > first_index:
        list[min_index], list[first_index] = list[first_index], list[min_index]
    # call a recursion with next first index till penultimate index
    if first_index < len(list) - 2:
        list = selection_sort_recursive(list, first_index + 1)
    return list


#bubble sort
def bubble_sort(list):
    # loop through list
    for i in range(len(list)):
        try:
            # next index
            j = i + 1
            # if current value > next value, swap elements
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
        except IndexError:
            # if next list index does not exists -> end of list, return
            return list