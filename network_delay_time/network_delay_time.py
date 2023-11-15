from collections import defaultdict
import heapq

def network_delay_time(times, n, source):
    # Convert the input edge data into an adjacency dict.
        # Iterate over the edges.
        # For each edge, add the target node (with weight) to the list of edges in the adjacency dict for the source node.
    graph = defaultdict(list)
    for src, dst, delay in times:
        graph[src].append((dst, delay))
    # print(graph)
    
    # Set up the data structures we'll need to track the minimum cost to each node.
        # Initialize a dict to track the minimum cost to each node. (reference implementation uses a list instead)
        # Initialize a set to track the nodes we have visited.
        # Initialize a priority queue to track the nodes we have yet to visit.'
    delays = {}
    visited = set()
    heap = [(0, source)]

    # Run Dijkstra's algorithm over the converted graph data, tracking the minimum cost to each node.
    while heap:
        delay, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        delays[node] = delay  # reference updates the delays speculative while examining neighbors

        for neighbor, ndelay in graph[node]:
            # this check is a micro-optimization on the growth of the heap and is not required
            if neighbor in visited:
                continue

            tdelay = delay + ndelay
            # if we speculatively update the delays here, then we _do_ need the less than check used by the reference implementation (which also acts a micro-optimization on the growth of the heap).
            heapq.heappush(heap, (tdelay, neighbor))

    # print(delays)

    # Upon completing Dijkstra's algorithm, we will have the minimum cost to each node. If there are nodes whose cost is still infinity, we know that we were unable to reach those nodes from the source node. Alternatively, we could check the length of the visited set against the number of nodes in the graph. If they are not equal, we know that we were unable to reach all of the nodes in the graph from the source node.
    # If not all nodes were reached, return -1. Otherwise, return the maximum cost from the minimum cost list. Dijkstra's algorithm finds minimum paths, but according to the challenge, we want to return the longest overall (how long it takes for every node to receive a signal). In other words, we are looking for the maximum minimum.
    if len(visited) < n:
        return -1

    return max(delays.values())
