import networkx as nx

# グラフの描画には Matplotlib を使う
from matplotlib import pyplot


def main():

    g = nx.Graph()

    # node をいくつか追加する
    g.add_nodes_from(['node', 'test'])

    # edge をいくつか追加する
    g.add_star([1, 2, 3, 4, 5, 6])
    g.add_star([6, 7, 8, 9, 10])

    # グラフを描画する
    nx.draw(g)

    # グラフを表示する
    pyplot.show()
    
    


if __name__ == '__main__':
    main()

