import itertools
from statistics import mean
from operator import itemgetter
import networkx as nx
from networkx.algorithms import bipartite


def get_deg_list_by_partition(graph, partition):
    """
    Get degree distribution for given partition of bipartite graph
    """
    if not bipartite.is_bipartite(graph):
        return []

    nodes = [node for node in graph.nodes if
             graph.nodes[node]['bipartite'] == partition]
    return bipartite.degrees(graph, nodes)[1]


def get_path_length_between_each_node(graph):
    """
    Get path length distribution for given graph
    """
    return nx.shortest_path_length(graph)


def get_connected_parts_dist(graph, partition):
    """
    Get degree distribution of each connected component, largest first,
    for given partition of bipartite graph
    """
    dist = []
    sorted_componensts = sorted(nx.connected_components(graph), key=len, reverse=True)
    subgraphs = [graph.subgraph(c).copy() for c in sorted_componensts]
    for s in subgraphs:
        degs = get_deg_list_by_partition(s, partition)
        if degs:
            dist.append(degs)

    return dist


def is_connected(graph):
    """
    Check if given graph is connected
    """
    return len(list(nx.connected_components(graph))) == 1


def get_parallel_edges_distribution(multi_graph):
    """
    Find out how often authors publish sth together
    """
    result = []
    for i, j in itertools.combinations(multi_graph.nodes(), 2):
        result.append(((i, j), multi_graph.number_of_edges(i, j)))

    return sorted(result, key=lambda x: x[1], reverse=True)


def get_mutual_pub_perc_distribution(pub_graph, auth_graph, min_pubs=3):
    """
    Find out how closely authors are intertwined
    """
    result = []
    authors_degs = get_deg_list_by_partition(pub_graph, 'authors')

    for i, j in itertools.combinations(auth_graph.nodes(), 2):
        i_deg = next((deg for auth, deg in authors_degs if auth == i), None)
        j_deg = next((deg for auth, deg in authors_degs if auth == j), None)
        assert i_deg and j_deg

        if i_deg >= min_pubs and j_deg >= min_pubs:
            mutual_pubs = auth_graph.number_of_edges(i, j)
            all_pubs = min(i_deg, j_deg)
            result.append(((i, j), mutual_pubs / all_pubs * 100))

    return sorted(result, key=lambda x: x[1], reverse=True)


def get_graph_density(graph):
    """
    Get density of given graph.
    For undirected graph is ranges from 0 (graph without edges) to 1 (complete graph).
    """
    return nx.density(graph)


def get_clustering_coef_mean(graph):
    """
    Get mean of graph nodes clustering coefficients
    """
    clustering_coefs = nx.clustering(graph)
    return mean(clustering_coefs.values())


def get_clustering_coef_dist(graph, min_deg=4):
    """
    Get clustering coefficient distribution for nodes with degree equals `min_deg` or greater
    """
    clustering_coefs = nx.clustering(graph)
    result = {auth: coef for auth, coef in clustering_coefs.items() if graph.degree(auth)
              >= min_deg}
    return result


def get_clustering_coef_list(graph, top_x=25):
    """
    Get `top_x` greatest clustering coefficients list
    """
    clustering_coefs = nx.clustering(graph)
    return dict(sorted(clustering_coefs.items(), key=itemgetter(1), reverse=True)[: top_x])
