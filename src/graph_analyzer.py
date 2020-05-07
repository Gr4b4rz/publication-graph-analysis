import networkx as nx
from networkx.algorithms import bipartite


class GraphAnalyzer:
    def __init__(self, graph_context):
        self.ctx = graph_context

    def get_deg_list_by_partition(self, partition):
        nodes = [node for node in self.ctx.publications_graph.nodes if
                 self.ctx.publications_graph.nodes[node]['bipartite'] == partition]
        return bipartite.degrees(self.ctx.publications_graph, nodes)[1]

    def is_bipartite(self):
        return bipartite.is_bipartite(self.ctx.publications_graph)

    def is_coherent(self):
        return True

    def get_coherent_edges_distribution(self):
        pass

    def get_path_length_between_each_node(self):
        return nx.shortest_path_length(self.ctx.co_authorship_graph)
