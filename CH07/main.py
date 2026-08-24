"""
Lab: Rooted & Compressed - Tree Traversal and Huffman Coding
COSC 2436 - Chapter 7

This starter code scaffolds three parts:
  Part 1: BFS vs DFS directory traversal
  Part 2: DFS vs BFS shortest-path counterexample (mango-seller style)
  Part 3: Mini Huffman coding (build tree, encode, decode)

Fill in every function marked with a TODO. Do not change function
signatures - the entry point at the bottom calls them exactly as written.
All input data below is hardcoded (no file I/O, no randomness) so the
lab runs the same way every time.
"""

from collections import deque
import heapq


# ---------------------------------------------------------------------------
# PART 1: File directory traversal (BFS vs DFS)
# ---------------------------------------------------------------------------

class DirNode:
    """A simple directory/file node used to build a tree (no real filesystem
    access is used here - this is a hardcoded tree so the lab is portable)."""

    def __init__(self, name, children=None):
        self.name = name
        # children is a list of DirNode objects (an empty list means a 'file')
        self.children = children if children is not None else []


def build_sample_directory():
    """Builds a small, hardcoded nested directory tree (>= 10 nodes) so
    students can compare BFS vs DFS traversal order without needing real
    files on disk."""
    # Leaf 'files'
    file1 = DirNode("notes.txt")
    file2 = DirNode("todo.txt")
    file3 = DirNode("photo.png")
    file4 = DirNode("song.mp3")
    file5 = DirNode("draft.docx")
    file6 = DirNode("index.html")
    file7 = DirNode("style.css")

    # Sub-folders
    docs = DirNode("docs", [file1, file2, file5])
    media = DirNode("media", [file3, file4])
    web = DirNode("web", [file6, file7])

    # Root (11 nodes total)
    root = DirNode("root", [docs, media, web])
    return root


def print_names_bfs(start_dir):
    """
    Print every node name in the tree using BREADTH-FIRST traversal.
    Use a deque and the book's queue/popleft pattern:
        queue = deque([start_dir])
        while queue:
            current = queue.popleft()
            print(current.name)
            for child in current.children:
                queue.append(child)

    NOTE: No 'searched' set is required here (unlike the Chapter 6
    mango-seller graph).
    """
    queue = deque([start_dir]) 

    while queue:
        current = queue.popleft()
        print(current.name)

        for child in current.children:
            queue.append(child)



def print_names_dfs(start_dir):
    """
    Print every node name in the tree using DEPTH-FIRST traversal.
    This should be RECURSIVE and needs no queue.
    """
    print(start_dir.name)

    for child in start_dir.children:
        print_names_dfs(child)


# ---------------------------------------------------------------------------
# PART 2: DFS fails at shortest path - counterexample
# ---------------------------------------------------------------------------

class TreeNode:
    """A binary tree node used for the mango-seller style counterexample."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_mango_tree():
    """
    Builds a small, hardcoded binary tree mirroring the book's diagram:
      - 'target' appears 3 levels deep on the LEFT branch
      - 'target' appears 1 level deep on the RIGHT branch
    DFS (which dives left first) will incorrectly return the farther
    target; BFS should correctly return the closer one.
    """
    # Left branch: root -> left -> left -> left = target (depth 3)
    left_leaf = TreeNode("target")
    left_level2 = TreeNode("L2", left=left_leaf)
    left_level1 = TreeNode("L1", left=left_level2)

    # Right branch: root -> right = target (depth 1)
    right_leaf = TreeNode("target")

    root = TreeNode("root", left=left_level1, right=right_leaf)
    return root


def dfs_search(root, target):
    """
    Depth-first search: recursively dive down the LEFT branch first,
    then the right, and return the FIRST node whose value == target
    that is found. Return None if not found.
    """
    if root is None:
        return None
    
    if root.value == target:
        return root

    left_result = dfs_search(root.left, target)

    if left_result is not None:
        return left_result
    
    return dfs_search(root.right, target)


def bfs_search(root, target):
    """
    Breadth-first search: use a queue (deque) to explore level by level
    and return the FIRST node whose value == target found at the
    shallowest depth. Return None if not found.
    """
    queue = deque([root]) if root is not None else deque()  

    while queue:
        current = queue.popleft()

        if current.value == target:
            return current

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return None
   


# ---------------------------------------------------------------------------
# PART 3: Mini Huffman coding
# ---------------------------------------------------------------------------

class HuffmanNode:
    """A node in the Huffman tree. Leaf nodes hold a character; internal
    nodes hold only a combined frequency and two children."""

    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Needed so heapq can order HuffmanNode objects by frequency.
        return self.freq < other.freq


def count_frequencies(text):
    """
    Count how many times each character appears in text.
    Return a dict like {'a': 3, 'b': 1, ...}.
    """
    freq_dict = {}
    
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1


    return freq_dict


def build_huffman_tree(freq_dict):
    """
    Build a Huffman tree from a frequency dictionary using the greedy
    approach with a heapq priority queue:
        1. Push a HuffmanNode(freq, char) for every character.
        2. While more than one node remains in the heap:
             - pop the two lowest-frequency nodes
             - combine them into a new internal node
               (freq = sum of the two, char=None, left=one, right=other)
             - push the new node back onto the heap
        3. Return the single remaining node (the tree root).
    """
    heap = []
    heapq.heapify(heap)  
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(freq, char))

    if len(heap) == 0:
        return None

    if len(heap) == 1:
        only = heapq.heappop(heap)
        return HuffmanNode(only.freq, left=only)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)

        heapq.heappush(heap, merged)

    return heap[0]
        
        
   
    


def generate_codes(root):
    """
    Walk the Huffman tree (left = '0', right = '1') to build a code table.
    Return a dict like {'a': '01', 'b': '1', ...}.
    Hint: a recursive helper that carries the 'path so far' as a string
    works well here.
    """
    codes = {}
    
    def helper(node, path):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = path if path else "0"
            return

        helper(node.left, path + "0")
        helper(node.right, path + "1")

    helper(root, "")
    return codes


def huffman_encode(text, codes):
    """
    Encode text into a single bitstring using the code table produced by
    generate_codes.
    """
    encoded = ""
    
    for char in text:
        encoded += codes[char]

    return encoded


def huffman_decode(encoded, root):
    """
    Decode a bitstring by walking the Huffman tree one bit at a time,
    starting over at the root each time a leaf is reached ('read like a
    tape').
    """
    decoded = ""
    current = root

    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded += current.char
            current = root

    return decoded


# ---------------------------------------------------------------------------
# Entry point - deterministic, hardcoded scaffolding (no file I/O, no random)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # ---- Part 1 ----
    print("Part 1: Directory traversal")
    sample_root = build_sample_directory()

    print("BFS order:")
    print_names_bfs(sample_root)

    print("DFS order:")
    print_names_dfs(sample_root)

    # BFS and DFS visit the same nodes, but BFS checks level by level while
    # DFS goes down one branch before moving to another. A searched set is not needed
    # because a tree has no cycles, so wont keep visiting the same node.

    # ---- Part 2 ----
    print("Part 2: DFS vs BFS shortest path counterexample")
    mango_root = build_mango_tree()

    dfs_result = dfs_search(mango_root, "target")
    bfs_result = bfs_search(mango_root, "target")

    print("DFS found target node:")
    print(dfs_result)
    print("BFS found target node:")
    print(bfs_result)

    # ---- Part 3 ----
    print("Part 3: Mini Huffman coding")
    sample_text = "huffman coding builds trees from frequencies"

    freqs = count_frequencies(sample_text)
    print("Character frequencies:")
    print(freqs)

    huffman_root = build_huffman_tree(freqs)
    codes = generate_codes(huffman_root)
    print("Code table:")
    print(codes)

    encoded_text = huffman_encode(sample_text, codes)
    print("Encoded bitstring:")
    print(encoded_text)

    decoded_text = huffman_decode(encoded_text, huffman_root)
    print("Decoded text:")
    print(decoded_text)

    print("Round trip matches original:")
    print(decoded_text == sample_text)

    # Reflection: compare compressed size to fixed-width baseline
    fixed_width_bits = 8 * len(sample_text)
    compressed_bits = len(encoded_text)
    print("Fixed-width bit count (8 times length of string):")
    print(fixed_width_bits)
    print("Compressed bit count:")
    print(compressed_bits)

    # TODO: more frequent characters get shorter huffman codes because they appear more often in text.
    # This reduces the total number of bits needed to store the encoded message.
