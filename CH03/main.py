"""
File System Explorer - Recursive Directory Search
COSC 2436 - Chapter 3: Recursion

This lab mirrors the book's "boxes within boxes" analogy using a
nested dictionary that represents a file system (folders containing
files and other folders).

You will implement four recursive functions:
    1. find_file(structure, target_name)
    2. count_files(structure)
    3. total_size(structure)
    4. print_tree_with_depth(structure, depth=0)  (stretch/bonus)

Remember the core recursion pattern from the reading:
    - BASE CASE: the simplest possible input (an empty folder, or a
      single file with no sub-contents) - this is where recursion STOPS.
    - RECURSIVE CASE: a folder that contains more items - this is where
      the function calls ITSELF on smaller pieces of the problem.

Missing a base case will cause infinite recursion (a stack overflow),
so be careful to always define one BEFORE writing the recursive case.
"""


# ---------------------------------------------------------------------------
# Provided helper functions (already implemented) - use these to visualize
# the call stack growing and shrinking as your recursive functions run.
# ---------------------------------------------------------------------------

def trace_enter(label, depth):
    """Print a message showing we are ENTERING a recursive call."""
    indent = "  " * depth
    print(indent + "-> entering: " + str(label))


def trace_exit(label, depth):
    """Print a message showing we are EXITING a recursive call."""
    indent = "  " * depth
    print(indent + "<- exiting: " + str(label))


# ---------------------------------------------------------------------------
# Task 1: find_file(structure, target_name)
# ---------------------------------------------------------------------------

def find_file(structure, target_name, current_path="", depth=0):
    """
    Recursively search the nested file system 'structure' for a file
    whose 'name' matches target_name. Return the full path (string) to
    the file if found, or None if it is not found anywhere.

    structure: a dict with keys:
        - "name": str
        - "type": "file" or "folder"
        - "size": int (only present when type == "file")
        - "contents": list of dicts (only present when type == "folder")

    Parallels the book's look_for_key() example.
    """
    # Build the path to this node so far (used for tracing and results)
    new_path = current_path + "/" + structure["name"]

    trace_enter(new_path, depth)

    if structure["type"] == "file":
        if structure["name"] == target_name:
            trace_exit(new_path + " (FOUND!)", depth)
            return new_path

        trace_exit(new_path, depth)
        return None

    if structure["type"] == "folder":
        for item in structure["contents"]:
            result = find_file(item, target_name, new_path, depth + 1)

            if result is not None:
                trace_exit(new_path, depth)
                return result

        trace_exit(new_path, depth)
        return None



   

    


# ---------------------------------------------------------------------------
# Task 2: count_files(structure)
# ---------------------------------------------------------------------------

def count_files(structure, depth=0):
    """
    Recursively count how many files (not folders) exist anywhere inside
    'structure', including files nested inside sub-folders.

    Identify the base case carefully:
        - a single "file" node contributes exactly 1 to the count
        - a "folder" node contributes the SUM of counts of its contents
          (an empty folder contributes 0)
    """
    trace_enter(structure["name"], depth)

    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return 1

    if structure["type"] == "folder":
        total = 0

        for item in structure["contents"]:
            total += count_files(item, depth + 1)
        
        trace_exit(structure["name"], depth)
        return total
    
    trace_exit(structure["name"], depth)
    return 0



# ---------------------------------------------------------------------------
# Task 3: total_size(structure)
# ---------------------------------------------------------------------------

def total_size(structure, depth=0):
    """
    Recursively sum the sizes of every file nested anywhere inside
    'structure'. This mirrors the fact(x) = x * fact(x-1) accumulation
    pattern, except we ADD sizes instead of multiplying.
    """
    trace_enter(structure["name"], depth)

    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return structure["size"]

    if structure["type"] == "folder":
        running_total = 0

        for item in structure["contents"]:
            running_total += total_size(item, depth + 1)
        
        trace_exit(structure["name"], depth)
        return running_total

    trace_exit(structure["name"], depth)
    return 0

    


# ---------------------------------------------------------------------------
# Task 4 (Stretch/Bonus): print_tree_with_depth(structure, depth=0)
# ---------------------------------------------------------------------------

def print_tree_with_depth(structure, depth=0):
    """
    Recursively print the file system tree, indenting each line based on
    how deeply nested it is (depth). Each recursive call should pass
    depth + 1 down to its children, so every stack frame has its OWN
    copy of the 'depth' variable (just like the fact() walkthrough in
    the reading).

    Example output style:
    root
      file1.txt
      subfolder1
        file2.txt
    """
    print( " " * depth + structure["name"])

    if structure["type"] == "file":
        return

    if structure["type"] == "folder":
        for item in structure["contents"]:
            print_tree_with_depth(item, depth + 1)




# ---------------------------------------------------------------------------
# Entry point - DO NOT remove. Uses a hardcoded nested file system so the
# program runs deterministically without reading any external files.
# ---------------------------------------------------------------------------

def build_sample_file_system():
    """Builds a hardcoded nested dictionary representing a file system."""
    file_system = {
        "name": "root",
        "type": "folder",
        "contents": [
            {"name": "readme.txt", "type": "file", "size": 5},
            {"name": "photo.jpg", "type": "file", "size": 200},
            {
                "name": "documents",
                "type": "folder",
                "contents": [
                    {"name": "resume.docx", "type": "file", "size": 15},
                    {"name": "cover_letter.docx", "type": "file", "size": 8},
                    {
                        "name": "taxes",
                        "type": "folder",
                        "contents": [
                            {"name": "2022.pdf", "type": "file", "size": 40},
                            {"name": "2023.pdf", "type": "file", "size": 42},
                        ],
                    },
                ],
            },
            {
                "name": "music",
                "type": "folder",
                "contents": [
                    {"name": "song1.mp3", "type": "file", "size": 30},
                    {"name": "song2.mp3", "type": "file", "size": 33},
                    {
                        "name": "playlists",
                        "type": "folder",
                        "contents": [
                            {"name": "workout.m3u", "type": "file", "size": 1},
                        ],
                    },
    ],
            },
            {
                "name": "empty_folder",
                "type": "folder",
                "contents": [],
            },
        ],
    }
    return file_system


if __name__ == "__main__":
    # Hardcoded, deterministic sample file system (10+ files/folders total)
    fs = build_sample_file_system()

    print("----- Task 1: find_file -----")
    result_path = find_file(fs, "2023.pdf")
    print(result_path)

    result_missing = find_file(fs, "does_not_exist.txt")
    print(result_missing)

    print("----- Task 2: count_files -----")
    num_files = count_files(fs)
    print(num_files)

    print("----- Task 3: total_size -----")
    size_sum = total_size(fs)
    print(size_sum)

    print("----- Task 4 (bonus): print_tree_with_depth -----")
    print_tree_with_depth(fs)
