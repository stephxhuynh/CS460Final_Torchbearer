# Development Log – The Torchbearer

**Student Name:** Steph Huynh
**Student ID:** 824058671

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – 5/7/2026: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

My initial plan is to begin the Dijkstra's precomputation design/algorithm such as the select_sources and run_dijkstra
which will be used to compute distances from the entrance and each relic chamber. 
I plan to implement that using the priority queue.
In this part, I expect the most difficult part will be to make sure my algorithm is 
efficient and has a good time complexity by handling the priority queue such as 
its duplicate entries to avoid extra work in my algorithm.
To test this, I can use the given tests graphs and run my dijkstra's on it to ensure that the program 
is outputting what is expected of it. I may also create my own testing to ensure that it is running
my algorithm efficiently by skipping said entries/nodes.

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

In my run_dijkstra function, I had a bug where it was not returning the correct distances
from the entrance to the relic chamber. I got: AssertionError: Test run_dijkstra FAILED: expected {'S': 0, 'B': 1, 'A': 3, 'E': 4}, got {'S': inf, 'B': 1, 'A': inf, 'E': inf}.
I used my own testing to ensure each function was working properly and found that my problem was in my run_dijkstra's function where the distances
were not being returned correctly. I fixed this by.... (continue here)

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
