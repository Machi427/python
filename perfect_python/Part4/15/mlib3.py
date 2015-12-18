import random
from matplotlib import pyplot

random.seed()

# random.random の代わりに normalvariate を使って乱数を生成する
r = [random.normalvariate(0.5, 0.2) for x in range(10000)]

pyplot.hist(r, 30)
pyplot.show()

