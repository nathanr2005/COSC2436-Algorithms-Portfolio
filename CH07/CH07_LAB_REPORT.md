# Lab Report — Chapter 7: Trees and Huffman Coding

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your BFS and DFS orders, your encode/decode round trip, and your bit counts.*

```
Part 1: Directory traversal
BFS order:
root
docs
media
web
notes.txt
todo.txt
draft.docx
photo.png
song.mp3
index.html
style.css

DFS order:
root
docs
notes.txt
todo.txt
draft.docx
media
photo.png
song.mp3
web
index.html
style.css

Part 2: DFS vs BFS shortest path counterexample
DFS found target node:
<__main__.TreeNode object>
BFS found target node:
<__main__.TreeNode object>

Part 3: Mini Huffman coding
Character frequencies:
{'h': 1, 'u': 3, 'f': 4, 'm': 2, 'a': 1, 'n': 3, ' ': 5, 'c': 2, 'o': 2, 'd': 2, 'i': 3, 'g': 1, 'b': 1, 'l': 1, 's': 3, 't': 1, 'r': 3, 'e': 5, 'q': 1}

Encoded bitstring:
111100100000000011100111110101001000100101011111011011101011110101000111110001011001101110111000101111111001011011101111000100001001110111100011111000100001111101000011110100111000011101001011011110

Decoded text:
huffman coding builds trees from frequencies

Round trip matches original:
True

Fixed-width bit count (8 times length of string):
352

Compressed bit count:
179

```

## Reflection Questions

1. **Explain the difference between BFS and DFS to someone who has never programmed.**
   - BFS searches one level at a time, kind of like searching each page in a book before going to the next. DFS follows one path as far it can go before trying the next path.

2. **Why do frequent letters get shorter codes? Use your own code table.** Frequent letters get shorter codes because they appear more often and uses fewer bits to save space. In my code table, the characters that appeared the most had shorter bits than the ones that appeared less often.
    

3. **Your decoder reads a stream of bits with no separators and still gets it right. Why is there never any ambiguity?**
Huffman codes are designed so that one characters codes is not the beginning of another character code. Because of this, decoder knows when it reaches a complete character and can continue reading the next one.
