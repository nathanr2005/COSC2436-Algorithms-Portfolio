# Lab Report — Chapter 4: Quicksort

*Complete both sections and commit this file with your code.*

## Test Results

The program tested quicksort on unsorted, sorted and reverse sorted lists using both strategies. The results showed that the pivot choice can have a huge effect on how well quicksort performs.

```text
Part 1: Divide & Conquer warm-ups
recursive_sum: 52
recursive_count: 12
recursive_max: 10
binary_search_recursive (target=8): 9
binary_search_recursive (target=99): -1

Part 2: Quicksort
first pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Part 3: Benchmark
shape             strategy    result
------------------------------------------------
unsorted          first       0.002042 s
unsorted          random      0.002377 s
sorted            first       RecursionError
sorted            random      0.002549 s
reverse sorted    first       RecursionError
reverse sorted    random      0.001386 s

```

## Reflection Questions

1. **Explain quicksort to someone who has never programmed.**
   -Quicksort is like organizing a pile of papers by choosing one as a pivot or reference point and then splitting the rest into groups. The pivot can also be known as the reference paper, and everything that belongs before it goes into one group the ones after into another group. Process keeps repeating until everything is in a group.

2. **A random pivot usually avoids the worst case. Why does randomness help here?**
A random pivot makes it less likely that the algorithm will keep choosing poor pivots that create an uneven group. It allows quicksort to split the list more efficiently, so it can avoid the worst-case behavior most of the time.

3. **Where does sorting show up in software you actually use?**
Sorting is used in shopping websites that organize their products by price, ratings or what kind of product they are. It is alos used when apps sort stuff like messages, files in computers and search results to have info easier to find.
