import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite
from itertools import combinations


class GraphContext:
    def __init__(self, path):
        self.original_df = pd.read_csv(path, delimiter=',')
        self._wut_authors = self._get_wut_authors()
        self._cleaned_df = self._get_cleaned_dataset()
        self._publications_graph = None
        self._co_authorship_graph = None
        self._simple_co_authorship_graph = None

    def _get_cleaned_dataset(self):
        cleaned_publications = pd.concat([pd.Series(row['Document Title'], row['Authors'].split('; '))
                                          for _, row in self.original_df.iterrows()]).reset_index()

        cleaned_publications.columns = ['Author', 'Title']
        # filter out authors not from WUT
        filtered_publications = cleaned_publications[cleaned_publications["Author"].isin(self._wut_authors)]
        return filtered_publications

    def _get_wut_authors(self):
        wut_affiliation = "Warsaw University of Technology"
        authors_affiliations_mapper = {}
        for _, row in self.original_df.iterrows():
            authors_affiliations_mapper.update(dict(zip(list(map(lambda x: x.strip(), row['Authors'].split(';'))),
                                             row['Author Affiliations'].split(';'))))
        return {author for author, affiliations in authors_affiliations_mapper.items()
                if wut_affiliation in affiliations}

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
            g = nx.MultiGraph()
            g.add_nodes_from(self._cleaned_df['Author'].unique().tolist())
            for edge in self._retrieve_co_authorship_graph_edges():
                g.add_edges_from(list(edge))
            self._co_authorship_graph = g
        return self._co_authorship_graph

    @property
    def simple_co_authorship_graph(self):
        if self._simple_co_authorship_graph is None:
            self._simple_co_authorship_graph = nx.Graph(self.co_authorship_graph)

        return self._simple_co_authorship_graph

    def _retrieve_co_authorship_graph_edges(self):
        return self.original_df.Authors.str.split('; ').apply(lambda x: combinations(x, 2)).tolist()
