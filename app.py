# app.py
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from graph_data import build_graph, ROADS
from dijkstra import dijkstra

st.title("🗺️ GPS Shortest Route Finder")
st.caption("Dijkstra's Algorithm with a min-heap")

graph = build_graph()
places = sorted(graph)

source = st.sidebar.selectbox("Source", places)
target = st.sidebar.selectbox("Destination", places, index=1)

if st.sidebar.button("Find Route"):
    path, distance, steps = dijkstra(graph, source, target)

    if path is None:
        st.error("No route found.")
    else:
        st.success(" → ".join(path))
        st.metric("Total distance", f"{distance} km")

        # Draw the map
        G = nx.Graph()
        for a, b, km in ROADS:
            G.add_edge(a, b, weight=km)
        pos = nx.spring_layout(G, seed=42)
        route_edges = list(zip(path, path[1:]))

        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue",
                edge_color="gray", node_size=1200, font_size=8, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=route_edges,
                               edge_color="red", width=3, ax=ax)
        nx.draw_networkx_edge_labels(
            G, pos, nx.get_edge_attributes(G, "weight"), font_size=8, ax=ax)
        st.pyplot(fig)

        st.subheader("Step-by-step: order in which places were visited")
        st.dataframe(pd.DataFrame(steps))