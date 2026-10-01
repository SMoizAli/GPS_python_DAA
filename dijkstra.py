# dijkstra.py
import heapq

def dijkstra(graph, source, target):
    dist = {node: float("inf") for node in graph}   # best known distance to each place
    prev = {node: None for node in graph}           # where we came from (to rebuild path)
    dist[source] = 0
    heap = [(0, source)]                            # (distance, place), smallest pops first
    steps = []                                      # saved for the step-by-step table

    while heap:
        d, u = heapq.heappop(heap)                  # take the closest unvisited place
        if d > dist[u]:                             # old, outdated entry, skip it
            continue
        steps.append({"Visited": u, "Distance": d})
        if u == target:                             # reached the destination, stop early
            break
        for v, w in graph[u]:                       # check every neighbor
            if d + w < dist[v]:                     # found a shorter way to v
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[target] == float("inf"):
        return None, float("inf"), steps            # no route exists

    path, node = [], target                         # walk backwards from destination
    while node is not None:
        path.append(node)
        node = prev[node]
    return path[::-1], dist[target], steps