# Lab Report — Chapter 9: Dijkstra's Algorithm

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — the costs table, the parents table, the path, and the
negative-weight result.*

```
=== Part 1: Book's Start/A/B/Finish graph ===
{'start': 0, 'a': 5, 'b': 2, 'finish': 6}
{'start': None, 'a': 'b', 'b': 'start', 'finish': 'a'}
['start', 'b', 'a', 'finish']

=== Part 2: Twin Peaks -> Golden Gate Bridge ===
BFS path (fewest hops):
['twin_peaks', 'a', 'b', 'golden_gate']
Dijkstra path (lowest cost):
['twin_peaks', 'c', 'd', 'e', 'golden_gate']
Dijkstra total cost:
12

=== Part 3: Negative-weight edge breaks Dijkstra ===
{'start': 0, 'a': 2, 'b': -8, 'finish': 6}
{'start': None, 'a': 'start', 'b': 'a', 'finish': 'b'}
['start', 'a', 'b', 'finish']

```

## Reflection Questions

1. **Explain Dijkstra's algorithm to someone who has never programmed.**
   - Dijkstras algorithm finds the cheapest path from one place to another. It checks different routes and keeps track of the lowest total cost.
 
2. **Why does the algorithm always pick the cheapest unprocessed node next, instead of going in order?** It picks up the cheapest unprocessed node because that is the best route it found so far. This helps it reach the lowest cost path efficiently.

3. **Where does the "cost" on an edge come from in real routing software, and how does changing what you measure change the answer without changing the algorithm?** The cost can represent things like travel time, distance or tolls. Changing the cost can make the algorithm choose a different route.
