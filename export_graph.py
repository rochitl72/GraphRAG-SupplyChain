import networkx as nx

# Load graph
G = nx.read_gpickle("../data/supply_chain_graph.gpickle")

# Export graph as JSON
nx.write_gml(G, "../data/supply_chain_graph.gml")
print("✅ Graph exported as 'data/supply_chain_graph.gml'")
