import networkx as nx

g = nx.Graph()

# パスを追加する
# この場合は、 add_edges_from([(1, 2), (2, 3), (3, 4)]) と等価
g.add_path([1, 2, 3, 4])

print(g.edges()) #=> [(1, 2), (2, 3), (3, 4)]


g = nx.Graph()

# 星構造を追加する
# リストの一つ目の node を中心に、それ以降の要素にそれぞれ edge を作る
# この場合は、 add_edges_from([(1, 2), (1, 3), (1, 4)]) と等価
g.add_star([1, 2, 3, 4])

print(g.edges()) #=> [(1, 2), (1, 3), (1, 4)]

