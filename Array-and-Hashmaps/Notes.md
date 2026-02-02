## Top K Frequent
Should try both approaches. Not just optimized

1. approach 1. iterate, count, use a heap. but this will be O of n log n because a heap lookup is 

2. iterate, store counts in hashmap, go through hashmap and store in frequency buckets where the index of the bucket is actually the count

## Leetcode 128 Longest Consecutive Sequence
1. approach is to sort nums. then iterate through nums counting the longest sequence. because sorting it is a time complexity of O(n log n) and because we ned to iterate through the sorted listed the final time complexity will be O(n) + O(n log n)

2. the best approach is to create a set from nums which will remove duplicates and create a O(1) lookup. we can then iterate through the set and identify if a number is the start of a sequence. if it is, see if the next value is in the set and continue to do so until the next value is not found. this results in a time complexity of O(n) and space complexity of O(n) (creating the new set)

### Product of array except self
1. iterate. create prefix storage O of n. Postfix storage O of n and results storage combining the prefix and postfix

2. reuse the results array saving on storage. populate with prefix then compute postfix

