import pytest
from src import GraphContext, GraphAnalyzer
import networkx as nx


class TestGraphLoading:
    ctx = GraphContext(path='resources/publications_test.csv')

    def test_graph_creation(self):
        assert self.ctx.publications_graph.number_of_nodes() == 12
        assert self.ctx.publications_graph.number_of_edges() == 15

        assert self.ctx.co_authorship_graph.number_of_nodes() == 9
        assert self.ctx.co_authorship_graph.number_of_edges() == 33

        assert self.ctx.simple_co_authorship_graph.number_of_nodes() == 9
        assert self.ctx.simple_co_authorship_graph.number_of_edges() == 27


class TestGraphAnalyzer:
    ctx = GraphContext(path='resources/publications_test.csv')
    analyzer = GraphAnalyzer(ctx)

    def test_degree_distibution(self):
        expected_pub_deg_list = [6, 6, 3]
        expected_auth_deg_list = [3, 3, 3, 1, 1, 1, 1, 1, 1]

        pub_deg_list = [num for (pub, num) in self.analyzer.get_deg_list_by_partition('titles')]
        assert sorted(pub_deg_list, reverse=True) == expected_pub_deg_list

        auth_deg_list = [num for (pub, num) in self.analyzer.get_deg_list_by_partition('authors')]
        assert sorted(auth_deg_list, reverse=True) == expected_auth_deg_list
