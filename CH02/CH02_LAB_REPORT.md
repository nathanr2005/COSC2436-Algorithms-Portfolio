# Lab Report — Chapter 2: Selection Sort

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your sorted lists and your ranked artist output.*

```text
I tested find_smallest, selection_sort, and rank_artists. The results showed that the lists have been sorted correctly and the artists were ranked from most to least played.

find_smallest results:
3
0
0

selection_sort results:
[2, 3, 5, 6, 10]
[]
[1, 4, 4]

original list after the selection_sort:
[9, 1, 5]

rank_artists results:
['Radiohead', 'Kishore Kumar', 'Wilco', 'Neutral Milk Hotel', 'Beck', 'The Strokes', 'The Black Keys']

```

## Reflection Questions

1. **Explain selection sort to someone who has never programmed.**
   - Selection sort is basically like sorting a deck of cards. You look through the cards, you find the smallest one, put it first, and then keep repeating the process with the cards that are left until everything is in order.

2. **Your list gets twice as long. Does selection sort do twice the work, or more?**
   - Selection sort would do more than twice the work because there would be twice as many passes, but each pass also has much more items to search through. As the list gets bigger, the amount of work grows much faster, which is why it has a running time of O(n^2).

3. **Chapter 2 says arrays are used more often than linked lists in practice. Based on what you built, why would that be?**  I think arrays are more useful because you can access an item immediately using its index instead of having 
