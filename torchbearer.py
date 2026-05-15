"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Steph Huynh
Student ID:   824058671

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """
    explanation = """
       - **Why a single shortest-path run from S is not enough:**
    Single shortest-path run is only for a direct path from S to exit (or directly to other relics) while ignoring possible stops on the way, meaning it
    gives us cost, no route to get there 

    - **What decision remains after all inter-location costs are known:**
    We need to still decide the optimal order to visit each relic to ultimately get to the exit.

    - **Why this requires a search over orders (one sentence):**
    Due to the one way corridors (directed path/graph),
    there can be multiple paths that produce different costs, so we go through
    all possible paths using our precomputation design to find the best minimum one.    
    """
    return explanation



# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    source = []

    # begin at spawn
    source.append(spawn)

    # add relics to sources; check for duplicates
    for r in relics:
        if r not in source:
            source.append(r)


    return source


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    graph_distance = {}
    # at start, set every node's distance to infinity
    for node in graph:
        graph_distance[node] = float('inf')

    # start distance from source to itself is 0
    graph_distance[source] = 0
    queue = [(0, source)]

    # while queue is not empty
    while queue:
        # pop the smallest distance/node from queue
        temp_distance, u = heapq.heappop(queue)
        # if we've already found a shorter distance, skip
        if temp_distance > graph_distance[u]:
            continue

        for neighbor, cost in graph[u]:
            new_distance = temp_distance + cost
            if new_distance < graph_distance[neighbor]:
                graph_distance[neighbor] = new_distance
                # push to queue with new distance/neighbors
                heapq.heappush(queue, (new_distance, neighbor))


    return graph_distance





def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    # get list of sources to map out
    sources_to_map = select_sources(spawn, relics, exit_node)
    # return dictionary after running run_dijkstra for each source
    return {source: run_dijkstra(graph,source) for source in sources_to_map}



# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    - **For nodes already finalized (in S):**
      - nodes 'v' in S with absolute/permanent minimum fuel/distance cost from source to the node.
    
    - **For nodes not yet finalized (not in S):**
      - recorded distance dist[u] is our best minimum fuel cost so far through safely finalized nodes, but could improve as we explore/finalize more nodes

    - **Initialization : why the invariant holds before iteration 1:**
      - Before the first iteration, S is empty so dist[x] is 0 because there are no nodes/paths in S yet and all other nodes are inf and not finalized.
    
    - **Maintenance : why finalizing the min-dist node is always correct:**
      - Cost is the permanent minimum cost from source to node when we finalize it
      - non-negative edge weights means an alternate (cheaper) path is not possible through non finalized nodes as distance can't be reduced later on.
      
    - **Termination : what the invariant guarantees when the algorithm ends:**
      - when queue is empty, all nodes are finalized and dist[x] is the minimum cost from source to node x
    
     - Torchbearer route decisions rely on correct finalized distances because if they're wrong, it doesn't truly find the shortest path if it wastes fuel or never finds a path with an exit. 

    
    
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
    Why Greedy Fails
    - **The failure mode:** Greedy fails when it only considers the immediate local optimal/cheapest steps without considering the future steps aka possible global optimal/cheapest steps.
    - **Counter-example setup:** (using illustration nodes): S = start/entrance, relics = B,C,D; exit = T; 
      - S--> B = 1; S-->C = 2; S-->D = 50; B-->C = 100; B-->D = 100;C-->D = 1; D-->B = 1; B-->T = 1; D-->T = 1; C-->T = 1.
    - **What greedy picks:** From S, greedy would pick B --> C --> D --> T (total fuel cost = 103)
    - **What optimal picks:** S-->C-->D-->B-->T (total fuel cost = 5)
    - **Why greedy loses:** Greedy only looks at the immediate next cheapest move, so we go to B, but that causes to have more expensive paths
    along the way. The total route cost involves all future steps, which greedy fails to consider.
    What the Algorithm Must Explore:
    - The algorithm must explore every possible relic order because different orders of relics can lead to different total fuel costs.

    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    # set up parameters reflecting 5a of readme and for _explore function; sets up starting search state
    relics_remaining = {}   # dictionary of relics remaining to be visited
    for relic in relics:
        relics_remaining[relic] = True
    relics_visited_order = []
    current_loc = spawn
    cost_so_far = 0
    # keep track of most optimal minimum cost and ordered list to get there
    best_cost = {
        'minimum_fuel_cost': float('inf'),
        'ordered_relic_list': []
    }
    # begin search
    _explore(dist_table, current_loc, relics_remaining, relics_visited_order, cost_so_far, exit_node, best_cost)


    return best_cost['minimum_fuel_cost'], best_cost['ordered_relic_list']


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    # pruning: "I plan to prune any route that I know costs more than what my current state/order is"
    # Best_so_far pruning from part 6
    lower_bound = cost_so_far
    if lower_bound >= best["minimum_fuel_cost"]:
        return


    # Explanation of why it is safe: The route can only increase from here,
        # so if lower_bound is more expensive than the current best global route, we can skip it without skipping the optimal solution,
        # which given we find a more optimal solution, is supposed to be less than the best["minimum_fuel_cost"].
        # We continue on to explore that possibility of a more optimal solution, but return if we know it's not an optimal solution.


    # base case: no relics to explore --> exit
    if len(relics_visited_order) == len(relics_remaining):
        # add up cost of route so far
        route_cost = cost_so_far + dist_table[current_loc][exit_node]

        # update best_so_far tracking: if the current route cost is less than the "best", replace it with that route and cost
        if route_cost < best["minimum_fuel_cost"]:
            best["minimum_fuel_cost"] = route_cost
            best["ordered_relic_list"] = relics_visited_order.copy()
        return



    # recursive: go through remaining relics
    for relic in relics_remaining:
        if relics_remaining[relic] == True:
            relics_remaining[relic] = False
            relics_visited_order.append(relic)

            # call recursion
            _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + dist_table[current_loc][relic], exit_node, best)

            # backtracking
            relics_visited_order.pop()
            relics_remaining[relic] = True



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    graph_distance = precompute_distances(graph, spawn, relics, exit_node)
    minimum_fuel_cost, ordered_relic_list = find_optimal_route(graph_distance, spawn, relics, exit_node)

    return (minimum_fuel_cost, ordered_relic_list)





# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

    # run custom test for select_sources and run_dijkstras
    graph = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }

    relics = ['B', 'C', 'D']

    sources = select_sources('S', relics , 'T')
    assert sources == ['S', 'B', 'C', 'D'], f"Test select_sources FAILED: expected ['S', 'B', 'C', 'D'], got {sources}"
    print(f" Test select_sources passed sources={sources}")

    distance = run_dijkstra(graph, 'S')
    expected_distance = {'S': 0, 'B': 1, 'C': 2, 'D': 2, 'T': 2}
    assert distance == expected_distance, f"Test run_dijkstra FAILED: expected {expected_distance}, got {distance}"
    print(f" Test run_dijkstra passed distances={distance}")

    # run custom test for precomputation
    dist_table = precompute_distances(graph, 'S', relics, 'T')
    expected_table = {
        'S': {'S': 0, 'B': 1, 'C': 2, 'D': 2, 'T': 2},
        'B': {'S': float('inf'), 'B': 0, 'C': 2, 'D': 1, 'T': 1},
        'C': {'S': float('inf'), 'B': 1, 'C': 0, 'D': 2, 'T': 1},
        'D': {'S': float('inf'), 'B': 1, 'C': 1, 'D': 0, 'T': 2}
    }
    assert dist_table == expected_table, f"Test precompute_distances FAILED: expected {expected_table}, got {dist_table}"
    print(f" Test precompute_distances passed dist_table={dist_table}")


    # Run tests on find_optimal_route (and therefore, _explore)
    cost, route = find_optimal_route(dist_table, 'S', relics, 'T')
    expected_cost = 4
    expected_route = ['B', 'D', 'C']

    assert cost == expected_cost, f"Test find_optimal_route FAILED: expected {expected_cost}, got {cost}"
    assert route == expected_route, f"Test find_optimal_route FAILED: expected {expected_route}, got {route}"
    print(f" Test find_optimal_route passed cost={cost}  route={route}")
