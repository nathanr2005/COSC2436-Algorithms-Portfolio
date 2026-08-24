"""
Pivot Points -- Building and Benchmarking Quicksort
Chapter 4: Divide and Conquer

This starter file scaffolds three parts:
  Part 1: D&C warm-up recursive functions
  Part 2: Quicksort implementation (standard + stretch pivot strategies)
  Part 3: Empirical benchmarking of quicksort on different input shapes

Fill in every TODO. Do not change the function signatures or the entry-point
guard at the bottom of this file.
"""

import time
import random


# ---------------------------------------------------------------------------
# PART 1: Divide & Conquer warm-ups
# ---------------------------------------------------------------------------

def recursive_sum(arr):
    """
    Recursively sum the elements of arr.

    Base case: TODO -- state the base case here (what does an empty list sum to?)
    Recursive case: TODO -- state how the problem shrinks each call
    """
    if not arr:
        return 0

    return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr):
    """
    Recursively count the number of elements in arr.

    Base case: TODO -- state the base case here
    Recursive case: TODO -- state how the problem shrinks each call
    """
    if not arr:
        return 0
    
    return 1 + recursive_count(arr[1:])


def recursive_max(arr):
    """
    Recursively find the maximum value in arr.

    Error case: an empty list has no maximum -- raise ValueError.
    Base case: TODO -- state the base case here (hint: single-element list)
    Recursive case: TODO -- state how the problem shrinks each call
    """
    if not arr:
        raise ValueError("recursive_max() requires a non-empty list")

    if len(arr) == 1:
        return arr[0]

    sub_max = recursive_max(arr[1:])

    if arr[0] > sub_max:
        return arr[0]
    else:
        return sub_max

def binary_search_recursive(arr, target):
    """
    Recursively search for target in a SORTED list arr.
    Return the index of target if found, else -1.

    Base case: TODO -- state the base case(s) here (empty search range, or found)
    Recursive case: TODO -- state how the search range shrinks each call
    """
    def helper(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            return helper(mid + 1, high)

        return helper(low, mid - 1)

    return helper(0, len(arr) - 1)


# ---------------------------------------------------------------------------
# PART 2: Quicksort
# ---------------------------------------------------------------------------

def quicksort(array, pivot_strategy="first"):
    """
    Sort array using the quicksort divide-and-conquer algorithm.
    Return a NEW list. Do not modify the caller's list.

    pivot_strategy: one of "first", "random", "middle"
        "first"  -- standard tier: pivot index 0
        "random" -- stretch tier: random.randrange(len(array))
        "middle" -- stretch tier: len(array) // 2
    Any other value must raise ValueError.

    Base case: TODO -- state the base case here (array length < 2)
    Recursive case: TODO -- state how the problem shrinks each call
    (pick pivot, partition into less/greater_or_equal, recurse, concatenate)
    """
    if len(array) < 2:
        return list(array)

    if pivot_strategy == "first":
        pivot_index = 0
    elif pivot_strategy == "random":
        pivot_index = random.randrange(len(array))
    elif pivot_strategy == "middle":
        pivot_index = len(array) // 2
    else:
        raise ValueError(f"Unknown pivot strategy: {pivot_strategy!r}")

    pivot = array[pivot_index]

    rest = (array[:pivot_index] + array[pivot_index + 1:])

    less = [value for value in rest if value < pivot]

    greater_or_equal = [value for value in rest if value >= pivot]

    return(quicksort(less, pivot_strategy) + [pivot] + quicksort(greater_or_equal, pivot_strategy))


# ---------------------------------------------------------------------------
# PART 3: Empirical worst-case vs average-case investigation
# ---------------------------------------------------------------------------

def measure_time(arr, pivot_strategy):
    """
    Time how long quicksort takes to sort a COPY of arr using the given
    pivot_strategy.

    Return:
      - the elapsed time in seconds (a nonnegative float), or
      - None if the sort reached Python's recursion limit.

    A poor pivot on already-ordered data produces one-sided partitions and a
    recursion depth of about n, which can exceed Python's limit. That is a real
    experimental result for this lab, not a bug -- report it, do not hide it by
    raising the global recursion limit.
    """
    start = time.perf_counter()

    try:
        result = quicksort(list(arr), pivot_strategy)
    except RecursionError:
        return None

    elapsed = time.perf_counter() - start

    if result != sorted(arr):
        raise RuntimeError("Quicksort produced an incorrect result")


    return elapsed


def run_benchmark(unsorted_list, sorted_list, reverse_sorted_list):
    """
    Run quicksort benchmarks on different input shapes.
    """
    input_shapes = {
        "unsorted": unsorted_list,
        "sorted": sorted_list,
        "reverse sorted": reverse_sorted_list,
    }

    pivot_strategies = ["first", "random"]

    print(f"{'shape':<18}{'strategy':<12}{'result':<18}")
    print("-" * 48)

    for shape_name, data in input_shapes.items():
        for strategy in pivot_strategies:
            elapsed = measure_time(data, strategy)

            if elapsed is None:
                result_text = "RecursionError"
            else:
                result_text = f"{elapsed:.6f} s"

            print(f"{shape_name:<18}{strategy:<12}{result_text:<18}")

    
    

# ---------------------------------------------------------------------------
# Entry point -- this scaffolding is already written for you. Do not change the
# function name, the data it builds, or the guard below.
# ---------------------------------------------------------------------------

def main():
    # Seeded so the random pivot and the shuffled list are reproducible for
    # everyone in the class.
    random.seed(42)

    sample_numbers = [4, 7, 1, 9, 3, 8, 2, 6, 5, 10, 0, -3]

    print("Part 1: Divide & Conquer warm-ups")
    print("recursive_sum:", recursive_sum(sample_numbers))
    print("recursive_count:", recursive_count(sample_numbers))
    print("recursive_max:", recursive_max(sample_numbers))

    sorted_sample = sorted(sample_numbers)

    print(
        "binary_search_recursive (target=8):",
        binary_search_recursive(sorted_sample, 8),
    )
    print(
        "binary_search_recursive (target=99):",
        binary_search_recursive(sorted_sample, 99),
    )

    print("\nPart 2: Quicksort")
    print("first pivot:", quicksort(sample_numbers, "first"))
    print("random pivot:", quicksort(sample_numbers, "random"))
    print("middle pivot:", quicksort(sample_numbers, "middle"))

    print("\nPart 3: Benchmark")

    # All three shapes hold the SAME values in different orders, so any timing
    # difference comes from the ordering and the pivot rule -- nothing else.
    n = 1000

    sorted_list = list(range(n))
    reverse_sorted_list = list(reversed(sorted_list))
    unsorted_list = sorted_list.copy()
    random.shuffle(unsorted_list)

    run_benchmark(
        unsorted_list,
        sorted_list,
        reverse_sorted_list,
    )


if __name__ == "__main__":
    main()
