from src import GraphContext, GraphAnalyzer


def main():
    ctx = GraphContext(path='resources/publications.csv')
    analyzer = GraphAnalyzer(ctx)

    # analyzer.get
    # print(analyzer.is_bipartite())
    # analyzer.get_deg_list_by_partition('titles')
    # analyzer.get_deg_list_by_partition('authors')
    # analyzer.get_path_length_between_each_node()


if __name__ == '__main__':
    main()
