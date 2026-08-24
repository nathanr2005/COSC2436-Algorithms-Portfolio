# Lab Report — Chapter 10: Greedy Algorithms

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your scheduling result, both knapsack answers side by side, your set cover, and your subset counts.*

```
Part 1: Scheduled classes
[('Art', 9.0, 10.0), ('English', 9.5, 10.5), ('Math', 10.0, 11.0), ('CS', 10.5, 11.5), ('Music', 11.0, 12.0)]

Part 2: Greedy knapsack choice
[('stereo', 3000, 4)]
Part 2: Greedy knapsack value
3000

Part 2: Brute-force knapsack choice
[('laptop', 2000, 3), ('guitar', 1500, 1)]
Part 2: Brute-force knapsack value
3500

Part 2: Gap between brute force and greedy
500

Part 3: Stations chosen, in order
['kone', 'ktwo', 'kthree', 'kfive']

Part 3: Exact solver combinations to check for 5 stations
32
Part 3: Exact solver combinations to check for 20 stations
1048576
Part 3: Exact solver combinations to check for 100 stations
1267650600228229401496703205376

Reflection
Huffman tree construction is another greedy algorithm because it repeatedly combines the 2 lowest frequency nodes. It is exactly optimal, not an approximation.

```

## Reflection Questions

1. **Explain the greedy strategy to someone who has never programmed.**
   - A greedy strategy picks the best choice available at each step. It keeps making choices until the problem is finished.

2. **Greedy was perfect for scheduling and wrong for the knapsack. What changed about the problem?** Scheduling works because picking the class that ends earliest leaves room for more classes. In the knapsack, picking the most valuable item first can prevent a better combination of items from fitting.

3. **You already wrote a greedy algorithm in an earlier lab — building the Huffman tree in Chapter 7 repeatedly merges the two lowest-frequency nodes. Is that one exactly optimal, or an approximation?** The huffman algorithm is exactly optimal. Merging the 2 lowest frequency nodes repeatedly produces the best compression.
