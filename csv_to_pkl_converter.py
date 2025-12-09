import networkx as nx
import pickle
import csv

# Directed graph for Bitcoin Alpha - CORRECT choice for trust networks
G = nx.DiGraph()

with open('soc-sign-bitcoinalpha.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        if len(row) < 4:
            continue

        try:
            source, target, rating, timestamp = row
            source = int(source)
            target = int(target)
            rating = int(rating)
            timestamp = int(timestamp)

            # Add edge with signed weight and timestamp
            G.add_edge(
                source, target,
                weight=1 if rating > 0 else -1,           # Signed weight (-10 to +10)
                timestamp=timestamp      # Temporal information
            )
        except (ValueError, IndexError) as e:
            print(f"Skipping malformed row: {row}")
            continue

# Save for SPMiner
with open('bitcoin_alpha.pkl', 'wb') as f:
    pickle.dump(G, f)

print("Graph saved successfully!")
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Graph type: {'Directed' if G.is_directed() else 'Undirected'}")
