# test_dijkstra.py
from graph_data import build_graph
from dijkstra import dijkstra

g = build_graph()

path, dist, _ = dijkstra(g, "Airport", "Stadium")
assert dist == 20
assert path == ["Airport", "Station", "Mall", "Hospital", "Stadium"]

path, dist, _ = dijkstra(g, "Airport", "Old Town")
assert dist == 18

path, dist, _ = dijkstra(g, "Airport", "Lake View")
assert dist == 24

path, dist, _ = dijkstra(g, "Mall", "Mall")
assert dist == 0

print("All tests passed!")