# graph_data.py
ROADS = [
    ("Airport", "Station", 8),
    ("Airport", "Tech Park", 12),
    ("Station", "Mall", 4),
    ("Station", "Market", 6),
    ("Tech Park", "Mall", 7),
    ("Tech Park", "University", 9),
    ("Mall", "Hospital", 3),
    ("Mall", "Market", 5),
    ("Market", "Old Town", 4),
    ("Hospital", "University", 6),
    ("Hospital", "Stadium", 5),
    ("University", "Lake View", 8),
    ("Stadium", "Lake View", 4),
    ("Old Town", "Stadium", 9),
    ("Old Town", "Hospital", 7),
]

def build_graph():
    graph = {}
    for a, b, km in ROADS:
        graph.setdefault(a, []).append((b, km))
        graph.setdefault(b, []).append((a, km))
    return graph