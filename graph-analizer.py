import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite


def get_cleaned_publications():
    raw_publications = pd.read_csv("publications.csv", delimiter=',')
    cleaned_publications = pd.concat([pd.Series(row['Document Title'], row['Authors'].split('; '))
                            for _, row in raw_publications.iterrows()]).reset_index()
    cleaned_publications.columns = ['Author', 'Title']
    return cleaned_publications


def get_publications_graph(publications):
    g = nx.cubical_graph()
    g.add_nodes_from(publications['Author'].unique().tolist())
    g.add_nodes_from(publications['Title'].unique().tolist())
    g.add_edges_from(publications.values.tolist())
    return g


def main():
    cleaned_publiccations = get_cleaned_publications()
    g = get_publications_graph(cleaned_publiccations)
    print(g.edges)
    print(g.nodes)


if __name__ == '__main__':
    main()