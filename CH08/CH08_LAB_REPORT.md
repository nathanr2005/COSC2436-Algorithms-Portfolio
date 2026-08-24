# Lab Report — Chapter 8: Balanced Trees

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — both tree heights, comparison counts, and the AVL result.*

```=== PART 1: Basic BST operations ===
[20, 30, 40, 50, 70]
3
True
3

=== PART 2: Same values, different insertion order ===
Tree A height: 4
Tree B height: 12
Tree A in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree B in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree A search comparisons for largest value: 3
Tree B search comparisons for largest value: 12

=== PART 3: AVL rotations fix the shape ===
AVL tree height after sorted insertion: 4

=== REFLECTION ===
See comments above for the reflection table.
.

```

## Reflection Questions

1. **Explain a binary search tree to someone who has never programmed.**
   - A binary search tree is like a higher or lower guessing game where each node holds a value. smaller values go left and larger values go right.

2. **A tree built from sorted input performs no better than a plain list. Explain why, using your own two trees.** Sorted input made my tree grow mostly in one direction instead of spreading out. This made it taller required more comparisons to search.

3. **Chapter 8 says balanced trees are used for database indexes. Based on what you built, why is a tree a good fit for that job?** a balanced tree keeps data organized so it can be searched quickly. It also allows new data to be added without having to rearrange everything.
