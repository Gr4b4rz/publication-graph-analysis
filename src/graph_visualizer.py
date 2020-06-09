import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from matplotlib.ticker import FormatStrFormatter


def plot_histogram(title, xlabel, data, ylabel="Liczba wystąpień", bins=None, log=False):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.hist(data, bins=bins, edgecolor='black', log=log)
    plt.show()


def show_degree_distribution(data, title, xlabel):
    authors_degrees = [deg for _, deg in data]
    plot_histogram(title=title, xlabel=xlabel,
                   data=authors_degrees, bins=len(authors_degrees), log=True)


def show_path_length_between_each_node_distribution(data):
    path_lengths = []
    for k, v in data:
        path_lengths.extend(v.values())
    plot_histogram(title="Rozkład długości drogi między wierzchołkami grafu współautorstwa",
                   xlabel="Długość drogi pomiędzy parami wierzchołków", data=path_lengths, bins=8)


def show_connected_parts_distribution(data, title):
    plot_histogram(title=title, xlabel="Liczba wierzchołków składowych spójnych",
                   data=data, bins=200)


def show_parallel_edges_distribution(data):
    parallel_edges_values = [val for _, val in data]
    grouped_values = Counter(parallel_edges_values)
    x_label = list(map(str, grouped_values.keys()))
    y_data = list(grouped_values.values())
    x_pos = np.arange(len(x_label))
    plt.figure()
    plt.title("Rozkład stopnia zwielokrotnienia równoległych krawędzi grafu współautorstwa")
    plt.xlabel("Stopien zwielokrotnienia")
    plt.ylabel("Liczba wystąpień")
    plt.yscale('log')
    plt.xticks(x_pos, x_label)
    plt.bar(x_pos, y_data)
    # plt.gca().invert_yaxis()
    plt.show()


def show_clustering_coef_distribution(data):
    plot_histogram(title="Rozkład współczynnika klasteryzacji wierzchołków",
                   xlabel="Współczynnik klasteryzacji",
                   data=data.values(), bins=10)


def show_mutual_pub_distribution(data):
    mutual_publications = [val for _, val in data]
    plot_histogram(title="Rozkład liczby wspólnych publikacji",
                   xlabel="Odsetek wspólnych publikacji",
                   data=mutual_publications, bins=20)
