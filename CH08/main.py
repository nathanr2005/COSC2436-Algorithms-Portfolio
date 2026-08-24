"""
Lab: "Out of Balance" -- Binary Search Trees and Why Shape Matters

Part 1: Build a working BST (insert, search, height, in_order)
Part 2: Watch a BST degenerate into a linked list on sorted input
Part 3: Rotate to fix it (single rotations you implement, double
        rotations provided pre-written, then avl_insert)

Determinism note: every value in this file is hardcoded. No randomness,
no file I/O -- so results (heights, comparison counts) are always the
same every time you run this file.
"""


class BSTNode:
    """A single node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------------------------------------------------------------------
# PART 1: Build a working BST
# ---------------------------------------------------------------------------

def insert(root, value):
    """
    Recursively insert `value` into the BST rooted at `root`.
    Returns the (possibly new) root of this subtree.

    Reminder: this is the SAME recursion shape as the Chapter 3 recursion
    lab -- base case is an empty spot (None), recursive case is
    "go left or go right" depending on the comparison.
    """
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root


def search(root, value):
    """
    Search for `value` starting at `root`.
    Returns a tuple: (found, comparisons)

    NOTE: fill in a short comment below explaining, in your own words,
    how this is the same idea as Chapter 1's binary search -- except we
    are walking left/right CHILD POINTERS instead of jumping to array
    indices with math.
    # TODO: This works like a binary search because each comparison tells us which side we can ignore. Instead of using array indexes, we move through the left or right child of the tree.
    """
    comparisons = 0
    node = root

    while node is not None:
        comparisons += 1

        if node.value == value:
            return (True, comparisons)
        elif value < node.value:
            node = node.left
        else:
            node = node.right

    return (False, comparisons)

        


def height(root):
    """
    Return the height of the tree rooted at `root`.
    An empty tree (None) has height 0. A single node has height 1.
    """
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def in_order(root, result=None):
    """
    In-order traversal (left, node, right). Returns a list of values in
    sorted order. This reuses the DFS pattern from the Chapter 7 lab.
    """
    if result is None:
        result = []

    if root is None:
        return result

    in_order(root.left, result)
    result.append(root.value)
    in_order(root.right, result)

    return result


# ---------------------------------------------------------------------------
# PART 2: Watch it degenerate (constructed counterexample)
# ---------------------------------------------------------------------------

def compare_bst_shapes():
    """
    Build TWO trees from the SAME twelve values:
      - Tree A: values inserted in the mixed order given below
      - Tree B: the SAME values, inserted in already-sorted order

    Print for both trees:
      - height
      - in-order traversal (these should come out IDENTICAL -- that's the point)
      - comparisons needed to search for the LARGEST value

    Tree B should end up looking like a linked list wearing a tree costume.
    """
    mixed_order = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65]
    sorted_order = sorted(mixed_order)
    largest_value = max(mixed_order)

    tree_a = None
    tree_b = None
   
    for value in mixed_order:
        tree_a = insert(tree_a, value)

    for value in sorted_order:
        tree_b = insert(tree_b, value)

    height_a = height(tree_a)
    height_b = height(tree_b)

    in_order_a = in_order(tree_a)
    in_order_b = in_order(tree_b)

    found_a, comparisons_a = search(tree_a, largest_value)
    found_b, comparisons_b = search(tree_b, largest_value)

    print("Tree A height:", height_a)
    print("Tree B height:", height_b)
    print("Tree A in-order:", in_order_a)
    print("Tree B in-order:", in_order_b)
    print("Tree A search comparisons for largest value:", comparisons_a)
    print("Tree B search comparisons for largest value:", comparisons_b)

    # Sorted input is bad for a plain bst because every new value is larger than the previous ones, so the tree keeps growing to the right. This makes the tree act like a linked list rather than a balanced tree.
    
    return tree_a, tree_b


# ---------------------------------------------------------------------------
# PART 3: Rotate to fix it
# ---------------------------------------------------------------------------

def balance_factor(node):
    """
    Return height(left subtree) - height(right subtree) for `node`.
    A balanced AVL node has a balance factor of -1, 0, or 1.
    """
    if node is None:
        return 0
    
    return height(node.left) - height(node.right)


def rotate_right(node):
    """
    Single RIGHT rotation (fixes the LL case).

    
        Before:                After:
              node                pivot
             /                   /    \
          pivot                 A     node
         /    \                        /
        A      B                      B
    """
    pivot = node.left
    node.left = pivot.right
    pivot.right = node

    return pivot


def rotate_left(node):
    """
    Single LEFT rotation (fixes the RR case).

    TODO: draw your own before/after diagram here as a comment, e.g.:
        Before:            After:
          node                pivot
             \               /    \
             pivot          node   B
             /   \             \
            A     B              A
    """
    pivot = node.right
    node.right = pivot.left
    pivot.left = node
    return pivot



def rotate_left_right(node):
    """
    Double rotation for the LR case (pre-written for you):
    rotate node.left LEFT first, then rotate node RIGHT.
    """
    node.left = rotate_left(node.left)
    return rotate_right(node)


def rotate_right_left(node):
    """
    Double rotation for the RL case (pre-written for you):
    rotate node.right RIGHT first, then rotate node LEFT.
    """
    node.right = rotate_right(node.right)
    return rotate_left(node)


def avl_insert(root, value):
    """
    Insert `value` like a normal BST insert, then rebalance on the way
    back up using rotations so the tree's height stays close to log2(n).

    Scope for this lab: implement the LL and RR (single rotation) cases
    yourself; the LR and RL (double rotation) cases are already wired up
    above using rotate_left_right / rotate_right_left.
    """
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = avl_insert(root.left, value)
    else:
        root.right = avl_insert(root.right, value)

    balance = balance_factor(root)

    if balance > 1 and value < root.left.value:
        return rotate_right(root)

    if balance < -1 and value >= root.right.value:
        return rotate_left(root)

    if balance > 1 and value >= root.left.value:
        return rotate_left_right(root)

    if balance < -1 and value < root.right.value:
        return rotate_right_left(root)

    return root


def avl_demo():
    """
    Re-insert the SAME sorted values from Part 2 (the worst case for a
    plain BST) but this time using avl_insert instead of insert.
    Print the resulting height and compare it to Part 2's Tree B height.
    """
    sorted_order = sorted([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65])
    avl_root = None
    
    for value in sorted_order:
        avl_root = avl_insert(avl_root, value)

    print("AVL tree height after sorted insertion:", height(avl_root))


# ---------------------------------------------------------------------------
# REFLECTION
# ---------------------------------------------------------------------------

def print_reflection():
    """
    Fill in the table below as comments, comparing search/insert cost for:
      - a sorted array
      - a linked list
      - a balanced BST
    Then explain, in a sentence or two, why a database stores its indexes
    as a tree rather than a sorted array.
    """
    # TODO: Sorted array   - search: O (log n)   insert: O(n)
    # TODO: Linked list    - search: O(n)   insert: O(1)
    # TODO: Balanced BST   - search: O(log n)   insert: O(log n)
    # TODO: A database uses a tree index because it can search and insert without having to shift elements like an array would
    print("See comments above for the reflection table.")


def main():
    print("=== PART 1: Basic BST operations ===")
    root = None
    starter_values = [50, 30, 70, 20, 40]
    for v in starter_values:
        root = insert(root, v)
    print(in_order(root))
    print(height(root))
    found, comparisons = search(root, 40)
    print(found)
    print(comparisons)

    print("=== PART 2: Same values, different insertion order ===")
    compare_bst_shapes()

    print("=== PART 3: AVL rotations fix the shape ===")
    avl_demo()

    print("=== REFLECTION ===")
    print_reflection()


if __name__ == "__main__":
    main()
