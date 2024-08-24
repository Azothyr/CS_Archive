from random import seed, sample
g_comparisons = 0


def make_data(data_size):  # DO NOT REMOVE OR MODIFY THIS FUNCTION
    """
    A generator for producing data_size random values
    """
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data


def linear_search(lyst, target):
    comparisons = 0
    found = False
    for value in lyst:
        if value == target:
            found = True
            comparisons += 1
            break
        else:
            comparisons += 1
    return found, comparisons


def binary_search(lyst, target):
    global g_comparisons
    found = False
    mid = int(len(lyst) / 2)
    if len(lyst) != 0:
        if lyst[mid] < target:
            g_comparisons += 1
            return binary_search(lyst[mid+1:], target)
        elif lyst[mid] > target:
            g_comparisons += 1
            return binary_search(lyst[:mid], target)
        if lyst[mid] == target:
            g_comparisons += 1
            found = True

    return found, g_comparisons


def jump_search(lyst, target):
    comparisons = 0
    found = False
    length = len(lyst)
    block_size = int(length ** 0.5)
    prev = 0
    step = block_size

    while prev < length and lyst[min(step, length) - 1] < target:
        prev = step
        step += block_size
        comparisons += 1

    for i in range(prev, min(step, length)):
        comparisons += 1
        if lyst[i] == target:
            found = True
            break

    return found, comparisons


def main():
    data = next(make_data(10))
    print(linear_search(data, 13))
    print(binary_search(data, 13))
    print(jump_search(data, 13))


if __name__ == "__main__":
    main()
