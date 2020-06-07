import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


def plot_percentage_histogram(title, xlabel, data, ylabel="Procentowy udział", bins=None, log=False):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.hist(data, weights=np.ones(len(data)) / len(data), bins=bins, edgecolor='black', log=log)
    plt.show()


def show_degree_distribution(data, title):
    authors_degrees = [deg for _, deg in data]
    plot_percentage_histogram(title=title, xlabel="Stopień wierzchołka",
                              ylabel="Procentowy udział", data=authors_degrees, bins=10)


def show_publications_degree_distribution(data):
    titles_degrees = [deg for _, deg in data]
    plot_percentage_histogram(title="Rozkład stopni wierzchołków tytułów", xlabel="Stopień wierzchołka",
                              ylabel="Procentowy udział", data=titles_degrees, bins=10)


def show_path_length_between_each_node_distribution(data):
    path_lengths = []
    for k, v in data:
        path_lengths.extend(v.values())
    plot_percentage_histogram(title="Rozkład długosci drogi między wierzchołkami grafu współautorstwa",
                              xlabel="Długość drogi", ylabel="Procentowy udział", data=path_lengths, bins=10)


def show_connected_parts_distribution(data, title):
    data = [len(item) for item in data]
    plot_percentage_histogram(title=title,xlabel="Liczba wierzchołków składowych spójnych dla publikacji",
                              ylabel="Procentowy udział", data=data, bins=200)


def show_parallel_edges_distribution(data):
    data = [val for _, val in data]
    plot_percentage_histogram(title="Rozkład stopnia zwielokrotnienia równoległych krawędzi grafu", xlabel="Stopien zwielokrotnienia",
                              ylabel="Procentowy udział", data=data, bins=2)


def show_clustering_coef_distribution(data):
    plot_percentage_histogram(title="Rozkład współczynnika klasteryzacji wierzchołków", xlabel="Współczynnik klasateryzacji",
                              ylabel="Procentowy udział", data=data.values(), bins=10)


def show_mutual_pub_distribution(data):
    mutual_publications = [val for _, val in data]
    plot_percentage_histogram(title="Rozkład liczby wspólnych publikacji",
                              xlabel="Liczba wspólnych publikacji",
                              ylabel="Procentowy udział", data=mutual_publications, bins=20)
