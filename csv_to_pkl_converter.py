import networkx as nx
import pickle
import csv

# Directed graph for Bitcoin OTC
G = nx.DiGraph()

with open('soc-sign-bitcoinalpha.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header

    for row in reader:
        if len(row) < 4:
            continue

        source, target, rating, timestamp = row
        rating = int(rating)

        G.add_edge(
            int(source),
            int(target),
            weight=rating,           # keep sign for SPMiner
            timestamp=int(timestamp) # optional, can be omitted
        )

# Save for SPMiner
with open('bitcoin_alpha.pkl', 'wb') as f:
    pickle.dump(G, f)

print("Graph saved!")
print("Nodes:", G.number_of_nodes(), "Edges:", G.number_of_edges())
