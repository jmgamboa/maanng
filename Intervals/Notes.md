1) Meeting Rooms (Easy)

Pattern: Sort + single pass overlap check

What you should learn

Normalize interval problems by sorting by start time

Overlap detection via previous end

Core invariant

After sorting by start: the only possible conflict for interval i is with interval i-1.

If start_i < end_{i-1} ⇒ overlap exists.

Typical implementation shape

Sort intervals by start.

Track prev_end = intervals[0].end.

For each next interval:

if interval.start < prev_end → return false

else prev_end = interval.end

Return true

2) Merge Intervals (Medium)

Pattern: Sort + build output by merging

What you should learn

“Merge as you go” using a current merged interval

When overlap occurs, extend the end with max

Core invariant

merged is always a list of non-overlapping intervals.

The last interval in merged is the merge of all processed intervals that overlap it.

Typical implementation shape

Sort by start.

Initialize merged = []

For each interval:

if merged empty or interval.start > merged[-1].end → append

else merged[-1].end = max(merged[-1].end, interval.end)

Return merged

3) Meeting Rooms II (Medium)

Pattern: Min-heap of end times (or two pointers with sorted starts/ends)

What you should learn

Track “resources in use” with a heap of earliest finishing meeting

Peak heap size = minimum rooms

Core invariant

Heap contains end times of meetings currently active.

Before scheduling a meeting starting at s, remove all ends <= s.

Typical implementation shape (heap)

Sort intervals by start.

Min-heap ends

For each meeting:

while ends not empty and ends[0] <= start: pop

push end

update ans = max(ans, len(ends))

Return ans

4) Insert Interval (Medium)

Pattern: Three-phase scan (left / merge / right)

What you should learn

Insert and merge without re-sorting if input is already sorted & non-overlapping

Clean “phase transitions” to avoid edge-case spaghetti

Core invariant

Output remains sorted and non-overlapping.

At any moment, newInterval represents the merge of itself with all overlapping intervals seen so far.

Typical implementation shape

Add all intervals ending before new.start (no overlap) → res

Merge all intervals overlapping new:

new.start = min(new.start, interval.start)

new.end = max(new.end, interval.end)

Append merged new

Append remaining intervals (starting after new.end)

Return res

5) Non-overlapping Intervals (Medium)

Pattern: Greedy by end time (minimum removals / maximum keep)

What you should learn

Convert “remove minimum” into “keep maximum non-overlapping”

Greedy choice: always keep the interval with smallest end to leave room

Core invariant

Among intervals considered so far, we keep a set with:

no overlaps, and

minimal possible current end for the same count kept

If overlap occurs, dropping the one with larger end is always safe.

Typical implementation shape
Option A (classic): sort by end

Sort intervals by end.

Count how many can be kept:

prev_end = -inf

if start >= prev_end: keep it, prev_end = end

Answer = n - kept

Option B (sort by start, decide which to remove)

Sort by start.

Track prev_end = intervals[0].end, removals = 0

For each next:

if start < prev_end:

overlap → removals++

prev_end = min(prev_end, end) (keep tighter end)

else prev_end = end

6) Minimum Interval to Include Each Query (Hard)

Pattern: Offline queries + min-heap by interval length (with active eligibility)

What you should learn

“Offline” trick: sort queries and intervals to control eligibility

Heap stores candidates; remove invalid ones lazily

Multiple keys: min by length, but validity depends on end >= query

Core invariant

When processing query q in increasing order:

Heap contains exactly the intervals with start <= q that have been added

After popping invalid (end < q), heap top is the shortest interval covering q

Typical implementation shape

Sort intervals by start ascending.

Sort queries ascending, keep original indices.

Use min-heap of (interval_length, interval_end) for intervals whose start <= q.

For each query q in sorted order:

Push all intervals with start <= q:

length = end - start + 1

push (length, end)

While heap not empty and heap[0].end < q: pop (doesn’t cover q)

If heap empty → answer is -1

Else answer is heap[0].length

Return answers in original query order