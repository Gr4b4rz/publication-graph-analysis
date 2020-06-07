import pytest
from src import GraphContext
from src import graph_analyzer as analyzer


class TestGraphLoading:
    """
    Test graph creation from csv file
    """
    ctx = GraphContext(path='resources/publications_test.csv')

    def test_graph_creation(self):
        assert self.ctx.publications_graph.number_of_nodes() == 12
        assert self.ctx.publications_graph.number_of_edges() == 15

        assert self.ctx.co_authorship_graph.number_of_nodes() == 9
        assert self.ctx.co_authorship_graph.number_of_edges() == 33

        assert self.ctx.simple_co_authorship_graph.number_of_nodes() == 9
        assert self.ctx.simple_co_authorship_graph.number_of_edges() == 27


class TestGraphAnalysis:
    """
    Test analysis of tiny network, which can verified with results computed manually
    """
    ctx = GraphContext(path='resources/publications_test.csv')

    def test_degree_distribution(self):
        expected_pub_deg_list = [6, 6, 3]
        expected_auth_deg_list = [3, 3, 3, 1, 1, 1, 1, 1, 1]

        pub_deg_list = [num for (pub, num) in
                        analyzer.get_deg_list_by_partition(self.ctx.publications_graph, 'titles')]
        assert sorted(pub_deg_list, reverse=True) == expected_pub_deg_list

        auth_deg_list = [num for (pub, num) in
                         analyzer.get_deg_list_by_partition(self.ctx.publications_graph, 'authors')]
        assert sorted(auth_deg_list, reverse=True) == expected_auth_deg_list

    def test_path_length_calculation(self):
        # According to guidelines, there should be co_authorship_graph,
        # but I think it must be simple_co_authorship_graph
        lengths = analyzer.get_path_length_between_each_node(self.ctx.simple_co_authorship_graph)
        # nothing to test ...
        assert lengths

    def test_graph_connectivity_check(self):
        assert analyzer.is_connected(self.ctx.publications_graph)
        self.ctx.publications_graph.remove_edge("publication1", "M. Lipka")
        assert not analyzer.is_connected(self.ctx.publications_graph)

        # cleanup
        self.ctx.publications_graph.add_edge("publication1", "M. Lipka")

    def test_subgraphs_degree_distribution(self):
        self.ctx.publications_graph.remove_edge("publication1", "M. Lipka")
        pub_dist = analyzer.get_connected_parts_dist(self.ctx.publications_graph, 'titles')
        auth_dist = analyzer.get_connected_parts_dist(self.ctx.publications_graph, 'authors')
        expected_pub_deg_list = [6, 5, 3]
        expected_max_auth_deg_list = [3, 3, 3, 1, 1, 1, 1, 1]
        expected_min_auth_deg_list = [0]
        assert pub_dist[0] == len(expected_pub_deg_list)
        assert auth_dist[0] == len(expected_max_auth_deg_list)
        assert auth_dist[1] == len(expected_min_auth_deg_list)

        # cleanup
        self.ctx.publications_graph.add_edge("publication1", "M. Lipka")

    def test_parallel_edges_distribution(self):
        result = analyzer.get_parallel_edges_distribution(self.ctx.co_authorship_graph)
        assert (('M. Parniak', 'M. Dąbrowski'), 3) in result
        assert (('M. Mazelanik', 'M. Dąbrowski'), 1) in result
        assert (('M. Mazelanik', 'P. Szewczak'), 0) in result

    def test_get_mutual_pub_perc_distribution(self):
        result = analyzer.get_mutual_pub_perc_distribution(
            self.ctx.publications_graph, self.ctx.co_authorship_graph, 1)

        assert (('M. Dąbrowski', 'M. Parniak'), 100.0) or (
            ('M. Parniak', 'M. Dąbrowski'), 100.0) in result
        assert (('M. Mazelanik', 'P. Szewczak'), 0.0) or (
            ('P. Szewczak', 'M. Mazelanik'), 0.0) in result

    def test_graph_density(self):
        result = analyzer.get_graph_density(self.ctx.simple_co_authorship_graph)
        assert result == (2 * 27) / (9 * 8)

    def test_get_clustering_coef_mean(self):
        result = analyzer.get_clustering_coef_mean(self.ctx.simple_co_authorship_graph)
        assert result == pytest.approx((3 * 19 / 28 + 6 * 1) / 9)

    def test_get_clustering_coef_dist(self):
        result = analyzer.get_clustering_coef_dist(self.ctx.simple_co_authorship_graph, min_deg=7)
        for author in {'M. Parniak', 'M. Dąbrowski', 'W. Wasilewski'}:
            assert author in result.keys()

    def test_get_clustering_coef_list(self):
        result = analyzer.get_clustering_coef_list(self.ctx.simple_co_authorship_graph, top_x=6)
        for author in {'M. Parniak', 'M. Dąbrowski', 'W. Wasilewski'}:
            assert author not in result.keys()
