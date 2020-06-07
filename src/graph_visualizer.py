import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from matplotlib.ticker import PercentFormatter, FormatStrFormatter


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
                              ylabel="Procentowy udział", data=authors_degrees, bins=len(authors_degrees), log=True)


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
    plot_percentage_histogram(title=title, xlabel="Liczba wierzchołków składowych spójnych",
                              ylabel="Procentowy udział", data=data, bins=200)


def show_parallel_edges_distribution(data):
    parallel_edges_values = [val for _, val in data]
    length = len(parallel_edges_values)
    grouped_values = Counter(parallel_edges_values)
    x_label = list(map(str, grouped_values.keys()))
    y_data = [item/length * 100 for item in grouped_values.values()]
    x_pos = np.arange(len(x_label))
    plt.figure()
    plt.title("Rozkład stopnia zwielokrotnienia równoległych krawędzi grafu")
    plt.xlabel("Stopien zwielokrotnienia")
    plt.ylabel("Procentowy udział")
    plt.xticks(x_pos, x_label)
    fmt = '%.0f%%'
    yticks = FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(yticks)
    plt.bar(x_pos, y_data)
    plt.gca().invert_xaxis()
    plt.show()


def show_clustering_coef_distribution(data):
    plot_percentage_histogram(title="Rozkład współczynnika klasteryzacji wierzchołków",
                              xlabel="Współczynnik klasteryzacji", ylabel="Procentowy udział",
                              data=data.values(), bins=10)


def show_mutual_pub_distribution(data):
    mutual_publications = [val for _, val in data]
    plot_percentage_histogram(title="Rozkład liczby wspólnych publikacji",
                              xlabel="Odsetek wspólnych publikacji",
                              ylabel="Procentowy udział", data=mutual_publications, bins=20, log=True)
