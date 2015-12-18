import networkx as nx


def main():

    g = nx.Graph()

    g.add_cycle(range(5))
    g.add_cycle(range(5, 10))
    g.add_node(20)

    # 循環しているノードのリストを返す
    print(nx.cycle_basis(g)) #=> [[1, 2, 3, 4, 0], [9, 8, 7, 6, 5]]

    # もう一つ循環を作ってみる
    g.add_edges_from([(0, 5), (3, 8)])

    # 循環しているノードが一つ増えている
    print(nx.cycle_basis(g)) #=> [[9, 8, 7, 6, 5],
                             #    [4, 3, 8, 7, 6, 5, 0],
                             #    [1, 2, 3, 8, 7, 6, 5, 0]]


if __name__ == '__main__':
    main()

