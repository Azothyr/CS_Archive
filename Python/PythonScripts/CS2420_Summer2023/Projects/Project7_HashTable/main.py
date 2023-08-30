import sys
import time
from hashmap import HashMap


cache = HashMap()
cache_hits = 0
function_calls = 0


def weight_on_cacheless(r, c):
    if r == 0 and c == 0:
        return 0.0
    supporting_weight = 0.0

    if c > 0:
        supporting_weight += 100 + (weight_on_cacheless(r - 1, c - 1) / 2.0)

    if c < r:
        supporting_weight += 100 + (weight_on_cacheless(r - 1, c) / 2.0)

    return supporting_weight


def weight_on_with_caching(r, c):
    global function_calls
    function_calls += 1
    try:
        global cache_hits
        hit_attempt = cache.get((r, c))
        cache_hits += 1
        return hit_attempt
    except KeyError:
        if r == 0 and c == 0:
            return 0.0
        supporting_weight = 0.0
        if c > 0:
            supporting_weight += 100 + (round(weight_on_with_caching(r - 1, c - 1) / 2.0, 2))
        if c < r:
            supporting_weight += 100 + (round(weight_on_with_caching(r - 1, c) / 2.0, 2))
        cache.set((r, c), supporting_weight)
        return supporting_weight


def main():
    global function_calls
    global cache_hits
    function_calls = 0
    cache_hits = 0

    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("cacheless.txt", "w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i, j))) + " "
            j += 1
        print(row)
        f.write(row + '\n')
        i += 1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.close()

    # Part 3 -- Use weight_on_with_caching() method
    print("\nWith Caching:")
    start = time.perf_counter()
    i = 0
    f = open("with_caching.txt", "w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_with_caching(i, j))) + " "
            j += 1
        print(row)
        f.write(row + '\n')
        i += 1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + "\n")
    print("\nNumber of functions calls: " + str(function_calls))
    f.write("\nNumber of functions calls: " + str(function_calls) + "\n")
    print("Number of cache hits: " + str(cache_hits))
    f.write("\nNumber of cache hits: " + str(cache_hits) + "\n")
    f.close()


if __name__ == "__main__":
    main()
