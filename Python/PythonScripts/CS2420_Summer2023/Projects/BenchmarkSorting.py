from random import seed, sample
compare_total = 0
swap_total = 0


def is_sorted(lyst):
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


def quicksort(lyst):
    global compare_total
    global swap_total
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")

    def partition(data, l_index, h_index):
        global compare_total
        global swap_total
        midpoint = int(l_index + (h_index - l_index) / 2)
        pivot = data[midpoint]

        complete = False
        while not complete:
            while data[l_index] < pivot:
                compare_total += 1
                l_index += 1
            while pivot < data[h_index]:
                compare_total += 1
                h_index -= 1
            if l_index >= h_index:
                compare_total += 1
                complete = True
            else:
                compare_total += 1
                temp = data[l_index]
                data[l_index] = data[h_index]
                data[h_index] = temp
                
                l_index += 1
                h_index -= 1
                swap_total += 1
        return h_index
    
    def sort(data, l_index, h_index):
        if l_index >= h_index:
            return
        end_index = partition(data, l_index, h_index)
        sort(data, l_index, end_index)
        sort(data, end_index + 1, h_index)

    low_index = 0
    high_index = len(lyst) - 1
    compare_total = 0
    swap_total = 0
    sort(lyst, low_index, high_index)

    return lyst, compare_total, swap_total


def selection_sort(lyst):
    global compare_total
    global swap_total
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")
    compare_total = 0
    swap_total = 0
    length = len(lyst)

    for i in range(length):
        sorting_index = i
        for j in range(i + 1, length):
            compare_total += 1
            if lyst[j] < lyst[sorting_index]:
                sorting_index = j
        temp = lyst[i]
        lyst[i] = lyst[sorting_index]
        lyst[sorting_index] = temp
        swap_total += 1

    return lyst, compare_total, swap_total


def insertion_sort(lyst):
    global compare_total
    global swap_total
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")
    compare_total = 0
    swap_total = 0
    length = len(lyst)

    for i in range(length):
        j = i + 1
        while j > 0 and j < length:
            if lyst[j] < lyst[j - 1]:
                temp = lyst[j]
                lyst[j] = lyst[j - 1]
                lyst[j - 1] = temp
                swap_total += 1
            compare_total += 1
            j -= 1
    return lyst, compare_total, swap_total


def mergesort(lyst):
    global compare_total
    global swap_total
    if not isinstance(lyst, list):
        raise TypeError(f"Error: Input data is a {type(lyst)}. Data must be a list.")
    compare_total = 0
    swap_total = 0
    length = len(lyst) - 1

    def merge(data, i, j, k):
        global compare_total
        global swap_total
        left_index = j - i + 1
        right_index = k - j
        left_partition = [0] * left_index
        right_partition = [0] * right_index

        for x in range(left_index):
            left_partition[x] = data[i + x]
        for y in range(right_index):
            right_partition[y] = data[j + 1 + y]

        merge_pos = i
        left_pos = 0
        right_pos = 0

        while left_pos < left_index and right_pos < right_index:
            compare_total += 1
            if left_partition[left_pos] <= right_partition[right_pos]:
                data[merge_pos] = left_partition[left_pos]
                swap_total += 1
                left_pos += 1
            else:
                data[merge_pos] = right_partition[right_pos]
                right_pos += 1
            merge_pos += 1

        while left_pos < left_index:
            compare_total += 1
            data[merge_pos] = left_partition[left_pos]
            left_pos += 1
            merge_pos += 1

        while right_pos < right_index:
            compare_total += 1
            data[merge_pos] = right_partition[right_pos]
            right_pos += 1
            merge_pos += 1

    def sort(data, i, k):
        if i < k:
            j = (i + k) // 2

            sort(data, i, j)
            sort(data, j + 1, k)
            merge(data, i, j, k)

    sort(lyst, 0, length)

    return lyst, compare_total, swap_total




def main():
    def make_data(data_size):
        seed(0)
        data = sample(range(data_size * 3), k=data_size)
        return data

    list_size = 10
    unsorted_list = make_data(list_size)
    function_list = [quicksort, selection_sort, insertion_sort, mergesort]
    argument_list = [(unsorted_list.copy(),), (unsorted_list.copy(),),
                     (unsorted_list.copy(),), (unsorted_list.copy(),)]
    for function, arguments in zip(function_list, argument_list):
        test = function(*arguments)
        print(test)
        print(f"{function.__name__} is correctly sorted = {is_sorted(test[0])}")

        """
        if cus_funcs == insertion_sort:
            break
        """


if __name__ == "__main__":
    main()
