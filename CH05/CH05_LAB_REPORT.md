# Lab Report — Chapter 5: Hash Tables

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your cache hit/miss output and your collision comparison.*

```
555-1234
Not found
Allowed to vote
Already voted!
Allowed to vote

MISS http://site.test/home
Contents of http://site.test/home
MISS http://site.test/about
Contents of http://site.test/about
HIT http://site.test/home
Contents of http://site.test/home
MISS http://site.test/contact
Contents of http://site.test/contact
HIT http://site.test/home
Contents of http://site.test/home

10
20
None
0.6

6
3
8
4

```

## Reflection Questions

1. **Explain a hash table to someone who has never programmed.**
   - A hash table is like a group of mailboxes where it holds information and placed in a specific box. It mainly just holds information and storage. Hash function is like the system that tellse you which mailobox information should go into.

2. **Chapter 5 says lookups are fast "on average." When is that not true, and what makes it go wrong?** Lookups can be slower when too many keys get placed into the same slot which causes collision. Fixing that makes it go to O(n) and you need a linked list to fix it.

3. **Your page cache avoided repeating expensive work. Where have you seen caching in software you use?** Caching happens in web browsers like accepting cookies, and when websites save information so they can load them faster next time you enter that website. Apps also cache images and other data so they dont have to download again.
