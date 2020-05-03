import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite
from itertools import combinations


class PublicationsGraphAnalyzer:
    def __init__(self, graph_context):
        self.graph_context = graph_context

    def get_degree_distribution_by_partition(self, partition):
        nodes = [node for node in self.graph_context.publications_graph.nodes if self.graph_context.publications_graph.nodes[node]['bipartite'] == partition]
        return bipartite.degrees(self.graph_context.publications_graph, nodes)[1]

    def is_bipartite(self):
        return bipartite.is_bipartite(self.graph_context.publications_graph)

    def is_coherent(self):
        return True

    def get_coherent_edges_distribution(self):
        pass

    def get_path_length_between_each_node(self):
        return nx.shortest_path_length(self.graph_context.co_authorship_graph)


class PublicationsGraphContext:
    def __init__(self, path):
        self.original_df = pd.read_csv(path, delimiter=',')
        self._cleaned_df = self._get_cleaned_dataset()
        self._publications_graph = None
        self._co_authorship_graph = None
        self._simple_co_authorship_graph = None

    def _get_cleaned_dataset(self):
        cleaned_publications = pd.concat([pd.Series(row['Document Title'], row['Authors'].split('; '))
                                          for _, row in self.original_df.iterrows()]).reset_index()
        cleaned_publications.columns = ['Author', 'Title']
        return cleaned_publications

    @property
    def raw_data(self):
        return self.original_df

    @property
    def publications_graph(self):
        if self._publications_graph is None:
            g = nx.Graph()
            g.add_nodes_from(self._cleaned_df['Author'].unique().tolist(), bipartite='authors')
            g.add_nodes_from(self._cleaned_df['Title'].unique().tolist(), bipartite='titles')
            g.add_edges_from(self._cleaned_df.values.tolist())
            self._publications_graph = g

        return self._publications_graph

    @property
    def co_authorship_graph(self):
        if self._co_authorship_graph is None:
            g = nx.Graph()
            g.add_nodes_from(self.original_df['Authors'].unique().tolist())
            for edge in self._retrieve_co_authorship_graph_edges():
                g.add_edges_from(list(edge))
            self._co_authorship_graph = g
        return self._co_authorship_graph

    @property
    def simple_co_authorship_graph(self):
        pass

    def _retrieve_co_authorship_graph_edges(self):
        return self.original_df.Authors.str.split('; ').apply(lambda x: combinations(x, 2)).tolist()


def main():
    graph_context = PublicationsGraphContext(path='publications.csv')
    analyzer = PublicationsGraphAnalyzer(graph_context)

    # analyzer.get
    # print(analyzer.is_bipartite())
    # analyzer.get_degree_distribution_by_partition('titles')
    # analyzer.get_degree_distribution_by_partition('publication')
    # analyzer.get_path_length_between_each_node()


if __name__ == '__main__':
    main()
