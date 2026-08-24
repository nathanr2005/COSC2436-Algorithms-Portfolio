# Lab Report — Chapter 12: K-Nearest Neighbors



## Test Results


```
[{'features': [6, 4], 'label': 'orange'}, {'features': [7, 3], 'label': 'orange'}]
orange
dog
cat
dog
standard
premium
likes
4.666666666666667
4.666666666666667

```

## Reflection Questions

1. **Explain k-nearest neighbors to someone who has never programmed.**
   - *"You're similar to the people around you" is the whole idea.* K-nearest neighbors looks at the people or items that are most similar to you. It uses those nearest neighbors to make a prediction about you.

2. **Two classmates pick k = 1 and k = 15 on the same data and get different answers. What is each one doing wrong, or right?** With k = 1, one unusual or incorrect neighbor can control the answer. With k = 15, too many neighbors are included, so overally majority can overpower closest matches.

3. **Chapter 12 says Netflix-style recommendations work this way. Describe how someone's viewing history becomes the "features."** someones viewing history can become features by using their ratings for different movies. Netflix can compare those features with other users to find people with similar tastes and recommend something they liked.
