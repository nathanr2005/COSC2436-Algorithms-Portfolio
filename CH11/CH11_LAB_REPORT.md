# Lab Report — Chapter 11: Dynamic Programming

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your call counts, your printed grid, and both string results.*

```
Part 1: Measure the waste
3
15
10
2040
18
332408
The call count roughly doubles each time another item is added.

Part 2: Fill the grid instead
Best value:
58

Naive call count:
332408

DP grid cells:
969

Part 3: Point the same technique somewhere else
hish vs fish:
Longest common substring: ish
Longest common subsequence: ish

hish vs vista:
Longest common substring: is
Longest common subsequence: is

A substring needs matching letters to be consecutive, but a subsequence can have gaps.

```

## Reflection Questions

1. **Explain dynamic programming to someone who has never programmed.**
   - *Writing answers down so you never solve the same problem twice is the core of it.*Dynamic programming saves answers to smaller problems so you dont have to solve them again. This makes solving a larger problem much faster.

2. **What has to be true about a problem for the grid to work at all?**
   - *Think about what the grid assumes about the subproblems.* The problem needs to be broken into smaller subproblems whose answers can be reused. Each part of the grid uses answers that were already calculated.

3. **Where does this show up in real software?**
   - *Spell-check suggestions, `git diff`, DNA sequence comparison — pick one and say how it maps.* git diff uses dynamic programming to compare two versions of a file. It finds similarities and differences without repeatedly doing the same comparisons.
