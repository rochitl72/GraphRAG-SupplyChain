import networkx as nx
import pandas as pd
import os
import pickle

# ✅ Load datasets
print("📥 Loading datasets...")
df_trade = pd.read_csv("../data/semiconductor_trade.csv")
df_stocks = pd.read_csv("../data/semiconductor_stock_prices.csv")
df_shipping = pd.read_csv("../data/shipping_data.csv")
df_events = pd.read_csv("../data/geopolitical_events.csv")

# ✅ Create a directed graph
G = nx.DiGraph()

### ✅ Add Country Nodes ###
print("🛠️ Adding country nodes...")
for country in set(df_trade["reporter"].tolist() + df_trade["partner"].tolist()):
    G.add_node(country, type="country")

### ✅ Add Trade Relationships (Edges) ###
print("🔗 Adding trade relationships...")
for _, row in df_trade.iterrows():
    G.add_edge(row["reporter"], row["partner"], weight=row["trade_value"])

### ✅ Add Company Nodes (NVIDIA, AMD, TSMC, ASML, Intel) ###
print("🏢 Adding semiconductor companies...")
companies = ["NVIDIA", "AMD", "TSMC", "ASML", "Intel"]
for company in companies:
    G.add_node(company, type="company")

# Link companies to key countries
for company in companies:
    for country in ["USA", "China", "Taiwan", "Germany", "Japan"]:
        G.add_edge(company, country, weight=1)

### ✅ Add Event Nodes ###
print("🌍 Adding geopolitical events...")
for _, row in df_events.iterrows():
    event_id = f"{row['event_type']}_{row['date']}"
    G.add_node(event_id, type="event", mentions=row["mentions"], severity=row["severity"])
    G.add_edge(event_id, "Global", weight=row["mentions"])

# ✅ Save graph
with open("../data/supply_chain_graph.gpickle", "wb") as f:
    pickle.dump(G, f)

print("✅ Graph construction complete! Graph saved as 'data/supply_chain_graph.gpickle'")
