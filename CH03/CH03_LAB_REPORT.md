# Lab Report — Chapter 3: Recursion

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output, including part of the call-stack trace.*

```This program was able to search through the folders recursively, count all files, calculate their total size, and print folder structure. Call stack trace also showed program going deeper into folders and then returning back.

----- Task 1: find_file -----
-> entering: /root
  -> entering: /root/readme.txt
  <- exiting: /root/readme.txt
  -> entering: /root/photo.jpg
  <- exiting: /root/photo.jpg
  -> entering: /root/documents
    -> entering: /root/documents/resume.docx
    <- exiting: /root/documents/resume.docx
    -> entering: /root/documents/cover_letter.docx
    <- exiting: /root/documents/cover_letter.docx
    -> entering: /root/documents/taxes
      -> entering: /root/documents/taxes/2022.pdf
      <- exiting: /root/documents/taxes/2022.pdf
      -> entering: /root/documents/taxes/2023.pdf
      <- exiting: /root/documents/taxes/2023.pdf (FOUND!)

      /root/documents/taxes/2023.pdf

Searching for does_not_exist.txt:
None

----- Task 2: count_files -----
9

----- Task 3: total_size -----
374

----- Task 4: print_tree_with_depth -----
root
 readme.txt
 photo.jpg
 documents
  resume.docx
  cover_letter.docx
  taxes
   2022.pdf
   2023.pdf
 music
  song1.mp3
  song2.mp3
  playlists
   workout.m3u
 empty_folder


```

## Reflection Questions

1. **Explain recursion to someone who has never programmed.**
   - Recursion is a function that calls itself to solve smaller parts of the current problem. Its like opening a tool box and seeing more tools in it over and over. Until you reach the bottom where theres no tools. The final one would be a base case which tells you theres no more stop now.

2. **An empty folder is a legitimate base case, not an error. 
An empty folder is still a normal folder it just contains nothing in it. If the program is treated as an error, it could stop the recursive search even there might be other folders and files to be searched.

3. **A folder nested 10,000 levels deep would crash your code. Why?**
 All recursive call gets added to the call stack while the program goes deeper each time. If there were thousands of nested folders, there would be way too many recursive calls on the stack and python would eventually reach its recursion limit.
