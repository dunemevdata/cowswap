import networkx as nx
import pandas as pd


df = pd.read_csv("cowswap_batch.csv.zip", compression='zip')


batch_count = 0
batch_without_cycle_count = 0

for txn_hash, txn_hash_df in df.groupby("tx_hash"):
    batch_count += 1
    
    G = nx.Graph()
    # add nodes and edges to the graph
    # each node is a token, and each edge is a swap between two tokens
    for index, row in txn_hash_df.iterrows():
        G.add_node(row['sell_token'])
        G.add_node(row['buy_token'])
        G.add_edge(row['sell_token'], row['buy_token'])
        
    # detect the cycles
    cycles = list(nx.cycle_basis(G))
    if len(cycles) == 0:
        batch_without_cycle_count += 1


print(f"Total batches: {batch_count}")
print(f"Total batches without cycles: {batch_without_cycle_count}")
print(f"Percentage of batches without cycles: {batch_without_cycle_count / batch_count * 100:.1f}%")
