import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# --- Exercise 1: linear search ---
def linear_search(arr, item):
    """
    Search for `item` in `arr` one element at a time.
    Returns a tuple: (index_found_or_None, number_of_steps_taken)
    """
    steps = 0

    for index, value in enumerate(arr):
        steps += 1
        if value == item:
            return index, steps
   
    return None, steps


# --- Exercise 2: binary search ---
def binary_search(arr, item):
    """
    Search for `item` in a SORTED `arr` by repeatedly checking the middle
    element and eliminating half the remaining items.
    Returns a tuple: (index_found_or_None, number_of_steps_taken)
    """
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1

        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid, steps
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None, steps


# --- Exercise 3: confirm step counts from the book's exercises ---
def max_steps_binary_search(n):
    """
    Build a sorted list of size n (values 0..n-1) and search for an item
    that is NOT present (worst case). Return only the number of steps taken.
    """
    arr = list(range(n))

    _, steps = binary_search(arr, -1)
    return steps



if __name__ == "__main__":
    # Hardcoded sample sorted list for basic testing (Exercises 1 & 2)
    sample_sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 89, 95]

    # TODO: call linear_search on sample_sorted_list for item 67, store the
    # returned (index, steps), and print both values
    found_index_linear, steps_linear = linear_search(sample_sorted_list, 67)
    
    print(found_index_linear)
    print(steps_linear)

    # TODO: call binary_search on sample_sorted_list for item 67, store the
    # returned (index, steps), and print both values
    found_index_binary, steps_binary = binary_search(sample_sorted_list, 67)

    print(found_index_binary)
    print(steps_binary)

    # --- Exercise 3: confirm step counts from the book's exercises ---
    book_sizes = (128, 256, 1024, 2048)
    for n in book_sizes:
        steps = max_steps_binary_search(n)
        
        naive_formula = math.ceil(math.log2(n)) + 1
        print(n)
        print(steps)
        print(naive_formula)

    # --- Exercise 4: empirical growth, linear vs. binary ---
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    linear_counts = []
    binary_counts = []

    for n in sizes:
        arr = list(range(n))
        _, l_steps = linear_search(arr, -1)
        _, b_steps = binary_search(arr, -1)

        linear_counts.append(l_steps)
        binary_counts.append(b_steps)

        print(n)
        print(l_steps)
        print(b_steps)

    # Plot comparisons vs n for both algorithms
    plt.figure(figsize=(8, 5))
   
    plt.plot(
        sizes,
        linear_counts,
        marker="o",
        label="Linear search: O(n)"
    )

    plt.plot(
    sizes,
    binary_counts,
    marker="o",
    label="Binary search: O(log n)"
    )

    plt.xscale("log")
    plt.xlabel("List size (n)")
    plt.ylabel("Comparisons (worst case)")
    plt.title("Growth of linear vs. binary search")
    plt.legend()
    plt.tight_layout()
    plt.close()

    # --- Exercise 5 (Bonus): verify step counts for 1024 vs 2048 names ---
    steps_1024 = max_steps_binary_search(1024)
    steps_2048 = max_steps_binary_search(2048)

    
    print(steps_1024)
    print(steps_2048)
