from src import GraphContext
from src import graph_analyzer as ga
from src import graph_visualizer as gv
from pprint import pprint


def main():
    ctx = GraphContext(path='resources/publications.csv')

    # rozkład stopni wierzchołków
    authors_degrees = ga.get_deg_list_by_partition(
        graph=ctx.publications_graph, partition='authors')
    gv.show_degree_distribution(data=authors_degrees, title="Rozkład stopni wierzchołków autorów")

    publications_degrees = ga.get_deg_list_by_partition(
        graph=ctx.publications_graph, partition='titles')
    gv.show_degree_distribution(data=publications_degrees,
                                title="Rozkład stopni wierzchołków publikacji")

    # Rozkład długości drogi między wierzchołkami dla grafu współautorstwa
    path_lengths = ga.get_path_length_between_each_node(graph=ctx.co_authorship_graph)
    gv.show_path_length_between_each_node_distribution(data=path_lengths)

    # Czy graf jest spójny?
    is_connected = ga.is_connected(graph=ctx.publications_graph)
    if is_connected:
        print("Analizowany graf jest spójny")
    else:
        print("Analizowany graf nie jest spójny")

    # Rozkład wierzchołków składowych spójnych
    authors_connected_parts = ga.get_connected_parts_dist(
        graph=ctx.publications_graph, partition='authors')
    print("Liczba składowych spójnych: {}".format(len(authors_connected_parts)))
    gv.show_connected_parts_distribution(
        data=authors_connected_parts, title="Rozkład liczby wierzchołków składowych spójnych autorów")

    publications_connected_parts = ga.get_connected_parts_dist(
        graph=ctx.publications_graph, partition='titles')
    gv.show_connected_parts_distribution(
        data=publications_connected_parts, title="Rozkład liczby wierzchołków składowych spójnych publikacji")

    # Dla grafu współautorstwa wyznaczyć rozkład stopnia zwielokrotnienia
    parallel_edges = ga.get_parallel_edges_distribution(multi_graph=ctx.publications_graph)
    gv.show_parallel_edges_distribution(data=parallel_edges)

    # Rozkład odsetka wspólnych publikacji
    mutual_pub = ga.get_mutual_pub_perc_distribution(
        pub_graph=ctx.publications_graph, auth_graph=ctx.co_authorship_graph)
    gv.show_mutual_pub_distribution(data=mutual_pub)

    # DLA GRAFU PROSTEGO
    # Obliczyć gęstość grafu
    e = ga.get_graph_density(ctx.simple_co_authorship_graph)
    print("Gęstość grafu:{}".format(e))

    # Wyznaczyć średnią wartość współczynnika klasteryzacji wierzchołków
    f = ga.get_clustering_coef_mean(ctx.simple_co_authorship_graph)
    print("Średnia wartość współczynnika klateryzacji wierzchołków: {}".format(f))

    # Wyznaczyć rozkład współczynnika klasteryzacji wierzchołków
    clustering_coef = ga.get_clustering_coef_dist(ctx.simple_co_authorship_graph)
    gv.show_clustering_coef_distribution(data=clustering_coef)

    # Wylistować współczynniki klasteryzacji wierzchołków dla 25
    print("Współczynniki klasteryzacji")
    pprint(ga.get_clustering_coef_list(ctx.simple_co_authorship_graph))


if __name__ == '__main__':
    main()
