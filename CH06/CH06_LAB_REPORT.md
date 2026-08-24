# Lab Report — Chapter 6: Breadth-First Search

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output for all three searches — reachable, distance, and full path.*

```True
True
2
['you', 'claire', 'thom', 'diego']
True
['create_repo_template', 'write_starter_code', 'write_tests', 'create_classroom_assignment', 'invite_students', 'grade_submissions']

```

## Reflection Questions

1. **Explain breadth-first search to someone who has never programmed.**
   - Breadth first search is like asking your frineds a question first, then asking other friends if nobody knows the answer. Queue keeps track of who needs to be checked first to make sure closest people are searched first.

2. **Two people in your network each know the other. Walk through what happens without the `searched` set.** Without the searched set, the program could keep going back and forth between the same 2 people. They would keep getting added to the queue which can run infinetly.

3. **Where does this show up in real software?**
   - *"People you may know," shortest routes, network hops — pick one and say how it maps.* Breadth first search can be used for features like people you may know on tiktok. It can search your friends first and then their friends to find people who are connected to you.
