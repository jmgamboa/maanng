- **Markov chain** — A stochastic process where the next state depends only on the current state (memoryless). **Example:** Weather model: `Sunny -> {Sunny 0.8, Rainy 0.2}`, then simulate day by day using those transition probabilities.

- **Dutch National Flag** — One-pass partitioning that groups items into 3 categories using three pointers (often used to sort 0/1/2). **Example:** For `[2,0,2,1,1,0]`, it rearranges to `[0,0,1,1,2,2]` in O(n).

- **Kruskal’s algorithm** — Builds a **minimum spanning tree (MST)** by repeatedly taking the cheapest edge that doesn’t form a cycle (uses Union-Find). **Example:** Sort edges by weight, add `(A-B,1)`, `(B-C,2)`, skip any edge that would close a cycle, until you have `V-1` edges.

- **Dijkstra’s algorithm** — Finds shortest paths from a source in graphs with **non-negative** edge weights using a priority queue. **Example:** Road map: starting at `S`, it keeps picking the currently-closest node and relaxing edges to compute shortest distances to all cities.

- **Prim’s algorithm** — Builds an **MST** by growing a tree from any start node, always adding the cheapest edge that connects the tree to a new node. **Example:** Start at `A`, pick min edge out of `{A-*}`, then repeat from the expanded tree until all vertices are included.

- **Manhattan distance** — Distance on a grid: sum of absolute coordinate differences (L1 metric). **Example:** From `(1,2)` to `(4,7)` is `|4-1| + |7-2| = 3 + 5 = 8`.

- **Kadane’s algorithm** — Computes maximum-sum contiguous subarray in O(n) using a running best ending-here vs global best. **Example:** For `[-2,1,-3,4,-1,2,1,-5,4]`, it returns `6` from subarray `[4,-1,2,1]`.

- **Floyd’s algorithm (Floyd–Warshall)** — All-pairs shortest paths via dynamic programming, trying each node as an intermediate (handles negative edges, not negative cycles). **Example:** With adjacency matrix `dist`, update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])` for all `k`, yielding shortest paths between every pair.