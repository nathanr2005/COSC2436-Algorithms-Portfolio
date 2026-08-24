"""
Lab Exercise: Selection Sort
Course: Introduction to Algorithms
Reference: Grokking Algorithms, Chapter 2 -- Selection Sort

Complete the TODOs below to implement:
  1. find_smallest(arr)
  2. selection_sort(arr)
  3. rank_artists(plays)
"""


def find_smallest(arr):
    """
    Return the INDEX of the smallest element in arr.

    Steps (from the text):
    - Assume the first element is the smallest to start.
    - Track both the smallest value seen so far and its index.
    - Loop over the remaining elements, updating both variables
      whenever a smaller value is found.
    - Return the index (not the value).
    """
    smallest_value = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    """
    Return a NEW list containing the elements of arr sorted from
    smallest to largest. The original list must NOT be modified.

    Steps (from the text):
    1. Make a copy of the input list so the original is not mutated.
    2. Create an empty result list.
    3. Loop once for each element: call find_smallest on the copy,
       pop that element out of the copy, and append it to the result.
    4. Return the result list.
    """
    arr_copy = arr[:]
    result = []

    while arr_copy:
        smallest_index = find_smallest(arr_copy)
        smallest_value = arr_copy.pop(smallest_index)
        result.append(smallest_value)

    return result


def rank_artists(plays):
    """
    plays: a dict mapping artist name -> play count

    Return a list of artist names ordered from MOST played to
    LEAST played. Reuse your selection sort logic.
    """
    remaining = list(plays.items())
    result = []

    while remaining:
        largest_index = 0
        largest_count = remaining[0][1]

        for i in range(1, len(remaining)):
            if remaining[i][1] > largest_count:
                largest_count = remaining[i][1]
                largest_index = i

        largest_pair = remaining.pop(largest_index)
        result.append(largest_pair[0])

    return result


if __name__ == "__main__":
    # ---- Part 1 tests: find_smallest ----
    print(find_smallest([5, 3, 6, 2, 10]))  # expected: 3
    print(find_smallest([1, 2, 3]))         # expected: 0
    print(find_smallest([7]))               # expected: 0

    # ---- Part 2 tests: selection_sort ----
    print(selection_sort([5, 3, 6, 2, 10]))
    # expected: [2, 3, 5, 6, 10]

    print(selection_sort([]))
    # expected: []

    print(selection_sort([4, 4, 1]))
    # expected: [1, 4, 4]

    original = [9, 1, 5]
    selection_sort(original)
    print(original)
    # expected: [9, 1, 5] (unchanged!)

    # ---- Part 3 test: rank_artists ----
    plays = {
        "Radiohead": 156,
        "Kishore Kumar": 141,
        "The Black Keys": 35,
        "Neutral Milk Hotel": 94,
        "Beck": 88,
        "The Strokes": 61,
        "Wilco": 111,
    }

    print(rank_artists(plays))
    # expected:
    # ['Radiohead', 'Kishore Kumar', 'Wilco',
    #  'Neutral Milk Hotel', 'Beck',
    #  'The Strokes', 'The Black Keys']


# ---- Part 4: Analysis Questions ----

# 1. find_smallest takes O(n) time, and selection sort calls it n times.
#    What is the overall running time?
#
#    Since find_smallest takes O(n) time and is called once for each
#    element, the overall running time is O(n^2).


# 2. On each pass, the copy shrinks: you check n elements, then n - 1,
#    then n - 2, and so on. On average you check about 1/2 * n elements
#    per pass. Why is the running time still written as O(n^2) rather
#    than O(1/2 * n^2)?
#
#    Big O ignores constant factors. Even though the average pass checks
#    about half of n, it still has the same growth rate as O(n^2).


# 3. Your implementation uses pop, which removes an element from the
#    middle of a list. Based on the array operation costs from Chapter 2,
#    what is the cost of that removal, and does it change the big O
#    running time of the sort?
#
#    Using pop() in the middle of a list takes O(n) time because the
#    other items have to be shifted over. It does not change the
#    overall O(n^2) running time.


# ---- Challenge (Optional): in-place selection sort ----
# Optional challenge not attempted.
