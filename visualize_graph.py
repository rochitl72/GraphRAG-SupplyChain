import networkx as nx
import matplotlib.pyplot as plt
import pickle
import os

# ✅ Get the correct file path
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
graph_path = os.path.join(base_dir, "../data/supply_chain_graph.gpickle")

# ✅ Load the graph
with open(graph_path, "rb") as f:
    G = pickle.load(f)

# ✅ Fix: Ensure Matplotlib works correctly
plt.switch_backend("TkAgg")  # Use TkAgg backend for compatibility

# ✅ Visualize the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Better layout
nx.draw_networkx_nodes(G, pos, node_size=50, node_color="blue")
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=8, font_color="black")

plt.title(f"Semiconductor Supply Chain Graph ({nx.number_of_nodes(G)} nodes, {nx.number_of_edges(G)} edges)")
plt.show()
