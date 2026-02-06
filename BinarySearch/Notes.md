The clean “pattern map” for each problem, in the same easiest → hardest progression, with what you should learn, the core invariant, and the typical implementation shape

1) Search a 2D Matrix (LC 74)

Pattern: Binary search on an implicitly 1D sorted structure
Teaches: Index mapping + standard BS template
Invariant: Treat matrix as sorted array where mid -> (r=mid//n, c=mid%n)
Shape:

lo=0, hi=m*n-1

compare matrix[mid//n][mid%n] with target

2) Find Minimum in Rotated Sorted Array (LC 153)

Pattern: Binary search on a rotated sorted array (pivot search)
Teaches: Using a reference (nums[hi] or nums[0]) to decide direction
Invariant: Minimum is always inside [lo, hi]; use sorted half detection
Common rule:

if nums[mid] > nums[hi], min is right

else min is left (including mid)

3) Find First and Last Position… (LC 34)

Pattern: Boundary binary search (lower_bound / upper_bound)
Teaches: “Find first true” style + off-by-one discipline
Invariant: Predicate is monotonic (e.g., nums[i] >= target)
Shape: Do two searches:

left = lower_bound(target) (first index with >= target)

right = lower_bound(target+ε) - 1 (or upper_bound(target)-1)

4) Koko Eating Bananas (LC 875)

Pattern: Binary search on the answer (monotonic feasibility)
Teaches: Turning a word problem into: “Is speed k enough?”
Invariant: If speed k works, any larger speed works (monotonic)
Predicate: hours(k) <= h where hours(k)=sum(ceil(p/k))
Shape:

lo=1, hi=max(piles)

mid -> compute hours -> move left/right

5) Search in Rotated Sorted Array (LC 33)

Pattern: Rotated array search target (case split + invariants)
Teaches: “One half is sorted” reasoning + target range checks
Invariant: At each step, one side [lo..mid] or [mid..hi] is sorted
Decision logic:

If left sorted: check if target in [nums[lo], nums[mid]) else go right

Else right sorted: check if target in (nums[mid], nums[hi]] else go left

6) Time Based Key-Value Store (LC 981)

Pattern: Data structure + binary search (per key timeline)
Teaches: Store monotonic timestamps, then query with upper_bound
Invariant: For each key, timestamps are sorted (append-only if sets come in order; otherwise still sort/insert)
Query: Get value with largest timestamp ≤ t
Shape:

dict[key] -> list of (timestamp, value)

get: binary search rightmost timestamp <= t (upper_bound(t) - 1)