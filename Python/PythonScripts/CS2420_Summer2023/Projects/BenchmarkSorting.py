from random import seed, sample


def is_sorted(lyst):
    print(f"is sorted working {lyst}")
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    confirmation = True
    prev_elem = lyst[0]
    for element in lyst:
        if not isinstance(element, int):
            raise TypeError(f"Error: Element: {element} at index: {lyst.index(element)} is a {type(element)}."
                            f" All elements in the list must be an integer.")
        if not element >= prev_elem:
            confirmation = False
        prev_elem = element

    return confirmation


def quicksort(lyst, low_index, high_index):
    print(f"quick working {lyst}")
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    def partition(data, l_index, h_index):
        midpoint = int(l_index + (h_index - l_index) / 2)
        pivot = data[midpoint]
        
        complete = False
        while not complete:
            print(h_index)
            # print(pivot)
            while data[l_index] < pivot:
                l_index += 1
            while pivot < data[h_index]:
                h_index += 1
            if l_index >= h_index:
                complete = True
            else:
                temp = data[l_index]
                data[l_index] = data[h_index]
                data[h_index] = temp
                
                l_index += 1
                h_index -= 1
        return h_index
    
    def sort(data, l_index, h_index):
        if l_index >= h_index:
            return
        end_index = partition(data, l_index, h_index)
        
        sort(data, l_index, end_index)
        sort(data, end_index + 1, h_index)

    # print(high_index)
    # print(len(lyst))
    list_sorted = sort(lyst, low_index, high_index)
    compare_total = 0
    swap_total = 0
    
    return list_sorted, compare_total, swap_total


def selection_sort(lyst, low_index, high_index):
    print(f"selection working {lyst}")
    return
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    list_sorted = []
    compare_total = 0
    swap_total = 0
    return list_sorted, compare_total, swap_total


def insertion_sort(lyst, low_index, high_index):
    print(f"insertion working {lyst}")
    return
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    list_sorted = []
    compare_total = 0
    swap_total = 0
    return list_sorted, compare_total, swap_total


def mergesort(lyst, low_index, high_index):
    print(f"merge working {lyst}")
    return
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    list_sorted = []
    compare_total = 0
    swap_total = 0
    return list_sorted, compare_total, swap_total


def main():
    def make_data(data_size):
        seed(1)
        data = sample(range(data_size * 3), k=data_size)
        return data
    
    unsorted_list = make_data(10)
    low_index = 0
    high_index = len(unsorted_list) - 1
    function_list = [quicksort, selection_sort, insertion_sort, mergesort]
    argument_list = [(unsorted_list, low_index, high_index), (unsorted_list, low_index, high_index),
                     (unsorted_list, low_index, high_index), (unsorted_list, low_index, high_index)]
    for function, arguments in zip(function_list, argument_list):
        test = function(*arguments)
        print(test)
        # print(is_sorted(test))


if __name__ == "__main__":
    main()
