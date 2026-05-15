# Development Log – The Torchbearer

**Student Name:** Steph Huynh
**Student ID:** 824058671

---

## Entry 1 – 5/7/2026: Initial Plan

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

## Entry 2 – 5/11/2026: bug in run_dijkstra

In my run_dijkstra function, I had a bug where it was not returning the correct distances
from the entrance to the relic chamber. I got: AssertionError: Test run_dijkstra FAILED: expected {'S': 0, 'B': 1, 'A': 3, 'E': 4}, got {'S': inf, 'B': 1, 'A': inf, 'E': inf}.
I used my own testing to ensure each function was working properly and found that my problem was in my run_dijkstra's function where the distances
were not being returned correctly. The source should
also be starting at 0, but it's printing inf still. I fixed this by
making sure I started source at 0 and adding heappush
to add the neighbor distances to the priority queue.

---

## Entry 3 – 5/12/26: next plan and implementation, difficulties, and testing

My next plan is to implement part 5-6 as we switch into creating our search and pruning algorithms.
I plan to implement part 5 ensuring I keep track of the state of the game (current location, relics, order of relics, cost so far).
I think the hardest part will be finding the different paths and ensuring that we choose the correct one (probably through backtracking), while also
making sure we keep track of the current state.
Part 6: I plan to prune any route that I know costs more than what my current state/order is, so we don't waste resources continuing down a bad path.
I plan to test this using my greedy problem from part 4, passing it 
to my algorithm to see if my algorithm correctly returned the global optimum rather than greedy optimum.



---

## Entry 4 – 5/13/26: Post-Implementation Reflection


I wonder if my implementation would've been good if there were more relics to go through.
I wonder what it would be like to solve this using dynamic programming instead similar to last midterm,
especially given that we could run into similar states and not have to recompute the same path.
That would be interesting to see how it would work, and if it would be faster or take up more time and space complexity.
I would want to try to implement it without a dictionary.
I think it is a bit repetitive to keep track of relic plus "true" or "false" for each relic.
We could do something similar to one of our (I believe) sliding window homework
where we keep track of the relics itself rather than pairing true/false with it.

---

## Final Entry – [Date]: Time Estimate

| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 1               |
| Part 2: Precomputation Design | 1               |
| Part 3: Algorithm Correctness | 1               |
| Part 4: Search Design | 1               |
| Part 5: State and Search Space | 1               |
| Part 6: Pruning | 1               |
| Part 7: Implementation | 5-6             |
| README and DEVLOG writing | 2               |
| **Total** |                 |
