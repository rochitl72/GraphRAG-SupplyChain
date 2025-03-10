from arango import ArangoClient
import networkx as nx
import pickle

# ✅ Connection Details
ARANGO_URL = "http://localhost:8529"
USERNAME = "root"
PASSWORD = "openSesame"
DB_NAME = "supply_chain_db"

# ✅ Connect to ArangoDB
client = ArangoClient(hosts=ARANGO_URL)
sys_db = client.db("_system", username=USERNAME, password=PASSWORD)

# ✅ Ensure the database exists
if not sys_db.has_database(DB_NAME):
    print(f"❌ Database '{DB_NAME}' not found. Exiting...")
    exit(1)

# ✅ Connect to the database
db = client.db(DB_NAME, username=USERNAME, password=PASSWORD)

# ✅ Load the NetworkX Graph
print("📥 Loading graph from gpickle file...")
with open("../data/supply_chain_graph.gpickle", "rb") as f:
    G = pickle.load(f)

# ✅ Create Collections if Not Exists
if not db.has_collection("nodes"):
    db.create_collection("nodes")

if not db.has_collection("edges"):
    db.create_collection("edges", edge=True)

# ✅ Store Nodes in ArangoDB
print("🔄 Uploading nodes...")
nodes_collection = db.collection("nodes")

for node, data in G.nodes(data=True):
    safe_key = str(node).replace(" ", "_")  # Fix key issue
    nodes_collection.insert({
        "_key": safe_key,
        "type": data.get("type", "unknown")
    }, overwrite=True)

# ✅ Store Edges in ArangoDB
print("🔗 Uploading edges...")
edges_collection = db.collection("edges")

for source, target, data in G.edges(data=True):
    safe_source = str(source).replace(" ", "_")
    safe_target = str(target).replace(" ", "_")
    edges_collection.insert({
        "_from": f"nodes/{safe_source}",
        "_to": f"nodes/{safe_target}",
        "weight": data.get("weight", 1)
    }, overwrite=True)

print("✅ Graph successfully stored in ArangoDB!")
