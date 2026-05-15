# The Torchbearer

**Student Name:** Steph Huynh 
**Student ID:** 824058671
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
    Single shortest-path run is only for a direct path from S to exit (or directly to other relics) while ignoring possible stops on the way, meaning it
    gives us cost, no route to get there
- **What decision remains after all inter-location costs are known:**
We need to still decide the optimal order to visit each relic to ultimately get to the exit.

- **Why this requires a search over orders (one sentence):**
Due to the one way corridors (directed path/graph), 
there can be multiple paths that produce different costs, so we go through
all possible paths using our precomputation design to find the best minimum one. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source                                                                |
|------------------|-----------------------------------------------------------------------------------|
| Spawn            | It's the starting point/fixed entrance point                                      |
| relic            | collecting relic --> relic becomes another start point to reach next point/relic. |

### Part 2b: Distance Storage


| Property | Your answer                                                                                            |
|---|--------------------------------------------------------------------------------------------------------|
| Data structure name | nested dictionary                                                                                      |
| What the keys represent | first key: source node. second key: destination                                                        |
| What the values represent | minimum fuel cost between each source and destination node                                             |
| Lookup time complexity | O(1)                                                                                                   |
| Why O(1) lookup is possible | hashing in data structure allows us to directly access/find such cost without having to search through |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(mlog(n)) 
- **Total complexity:** O((k+1)*mlog(n))
- **Justification (one line):** Use dijkstra's algorithm to find the minimum cost from each source node to each destination node (k relic) 

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  - nodes 'v' in S with absolute/permanent minimum fuel/distance cost from source to the node.

- **For nodes not yet finalized (not in S):**
  - recorded distance dist[u] is our best minimum fuel cost so far through safely finalized nodes, but could improve as we explore/finalize more nodes

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  - Before the first iteration, S is empty so dist[x] is 0 because there are no nodes/paths in S yet and all other nodes are inf and not finalized.

- **Maintenance : why finalizing the min-dist node is always correct:**
  - Cost is the permanent minimum cost from source to node when we finalize it
  - non-negative edge weights means an alternate (cheaper) path is not possible through non finalized nodes as distance can't be reduced later on.
  
- **Termination : what the invariant guarantees when the algorithm ends:**
  - when queue is empty, all nodes are finalized and dist[x] is the minimum cost from source to node x

### Part 3c: Why This Matters for the Route Planner

 - Torchbearer route decisions rely on correct finalized distances because if they're wrong, it doesn't truly find the shortest path if it wastes fuel or never finds a path with an exit. 

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy fails when it only considers the immediate local optimal/cheapest steps without considering the future steps aka possible global optimal/cheapest steps.
- **Counter-example setup:** (using illustration nodes): S = start/entrance, relics = B,C,D; exit = T; 
  - S--> B = 1; S-->C = 2; S-->D = 50; B-->C = 100; B-->D = 100;C-->D = 1; D-->B = 1; B-->T = 1; D-->T = 1; C-->T = 1.
- **What greedy picks:** From S, greedy would pick B --> C --> D --> T (total fuel cost = 103)
- **What optimal picks:** S-->C-->D-->B-->T (total fuel cost = 5)
- **Why greedy loses:** Greedy only looks at the immediate next cheapest move, so we go to B, but that causes to have more expensive paths
along the way. The total route cost involves all future steps, which greedy fails to consider.

### What the Algorithm Must Explore


- The algorithm must explore every possible relic order because different orders of relics can lead to different total fuel costs.

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component | Variable name in code | Data type  | Description                                |
|---|-----------------------|------------|--------------------------------------------|
| Current location | current_loc           | node       | current node of state space                |
| Relics already collected | relics_visited_order  | list[node] | List and order of relics collected so far  |
| Fuel cost so far | cost_so_far           | float      | total fuel cost from source to current_loc |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer                                                                                                                                                                                   |
|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data structure chosen | dictionary                                                                                                                                                                                    |
| Operation: check if relic already collected | Time complexity: O(1)                                                                                                                                                                         |
| Operation: mark a relic as collected | Time complexity:    O(1)                                                                                                                                                                      |
| Operation: unmark a relic (backtrack) | Time complexity:     O(1)                                                                                                                                                                     |
| Why this structure fits | A dictionary allows us to use constant time during each operation of checking, removing, adding, backtracking relic orders. We use True/False to keep track of what still needs to be visited |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** O(k!) where k is number of relics in |M|
- **Why:** To get the most optimal minimum fuel cost order, we must consider all possible orders of k relics.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** Tracks 'minimum_fuel_cost' and 'ordered_relic_list'; lowest fuel cost and ordered relic list so far.
- **When it is used:** In _explore() function 
- **What it allows the algorithm to skip:** skip nodes that are worst than the best-so-far tracking

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** current_loc, relics_visited_order, cost_so_far, relics_remaining, best['minimum_fuel_cost', 'ordered_relic_list]
- **What the lower bound accounts for:** cost_so_far to current state
- **Why it never overestimates:** Lower bound is equal to cost_so_far and can only increase as we explore more nodes/go towards final route. 

### Part 6c: Pruning Correctness

- if cost-so-far/lower bound is greater than route-cost (best-so-far), there's no point of exploring that path, knowing it's more expensive.
- impossible to get a better solution if we already know it's worse, so we can safely skip it.

---

## References
- lecture notes and homework problems (greedy algorithms, backtracking, dijkstra, etc)
