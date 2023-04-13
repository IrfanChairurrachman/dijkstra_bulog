import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def get_total(G, source, target, cutoff=2):
    route, total = [], []
    path = nx.all_simple_paths(G, source=source, target=target, cutoff=cutoff)

    for p in path:
        le = nx.path_weight(G, p, weight="weight")
        route.append(p)
        total.append(le)

    df = pd.DataFrame({'route': route, 'total': total})

    return df.sort_values(by = 'total')

def visualize_graph(Graf, position = 'shell'):

    if position == 'spring':
        pos = nx.spring_layout(Graf)
    elif position == 'spectral':
        pos = nx.spectral_layout(Graf)
    elif position == 'circular':
        pos = nx.circular_layout(Graf)
    elif position == 'planar':
        pos = nx.planar_layout(Graf)
    else:
        pos = nx.shell_layout(Graf)
    
    nx.draw_networkx_nodes(Graf, pos,node_size=600)

    nx.draw_networkx_edges(Graf, pos, width=1)

    nx.draw_networkx_labels(Graf, pos, font_size=8, font_family='sans-serif')

    edge_labels = nx.get_edge_attributes(Graf, 'weight')
    nx.draw_networkx_edge_labels(Graf, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.01)
    plt.tight_layout()
    plt.show()