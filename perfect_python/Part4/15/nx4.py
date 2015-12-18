import networkx as nx


def main():

    g = nx.Graph()

    g.add_star(range(5))
    g.add_star(range(5, 10))
    g.add_node('aaaa')

    # 接続されているノードごとのまとまりに分ける関数: connected_components
    print(nx.connected_components(g)) #=> [[0, 1, 2, 3, 4], [8, 9, 5, 6, 7], ['aaaa']]

    # ここで、 'aaaa' を 1 と繋げてみる
    g.add_edge(1, 'aaaa')

    # 'aaaa' が一つ目のグループに組み込まれる
    print(nx.connected_components(g)) #=> [[0, 1, 2, 3, 4, 'aaaa'], [8, 9, 5, 6, 7]]


if __name__ == '__main__':
    main()

