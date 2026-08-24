# Lab Report — Chapter 1: Binary Search


## Test Results

*Paste your printed step counts and describe what your growth chart shows.*

```I tested both linear search and binary search using the sampled sorted lits. I aswell tested both algorithms with increasingly larger lists to compare how the number of their steps grow.

Linear search for 67:
Index: 9
Steps: 10

Binary search for 67:
Index: 9
steps: 2

Binary search worst-case tests:
128 itmes: 7 steps
256 items: 8 steps
1024 items: 10 steps
2048 items: 11 steps

Growth comparisons:
n = 10     | Linear: 10      | binary: 3
n = 100    | Linear: 100     | binary: 6
n = 1000   | Linear: 1000    | binary: 9
n = 10000  | Linear: 10000   | binary: 13
n = 100000 | Linear: 100000  | binary: 16
n = 1000000| Linear: 1000000 | binary: 19

```

## Reflection Questions

1. **Explain binary search to someone who has never programmed.**
   -Binary search is similar to looking for someones name in a phone book. Insteadd of starting at the first name and checking one by one, you can open it near the middle and eliminates the other half until you find it.

2. **Doubling the list adds only one step to binary search. Why does that happen?**
   - Binary search eliminates about half of the remaining list every time it makes a guess. Each step cuts the amount of data left to search in half.

3. **Where does binary search show up in real software?**
Binary search can be useful in software whenever sorted info needs to be search efficiently. For example, a program could use binary search to find a value in a large collection without checking each item individually.
