import math

import numpy
import scipy
from scipy import interpolate
import pylab


def main():

    xs = numpy.linspace(0, 2*math.pi, 10)
    ys = numpy.sin(xs)
    
    # 先程のパラメータに加え、補間のなめらかさを指定する
    ius = interpolate.InterpolatedUnivariateSpline(xs, ys, k=1)

    xn = numpy.linspace(0, 2*math.pi, 180)
    yn = ius(xn)

    pylab.plot(xs, ys, 'o-', xn, yn)
    pylab.show()


if __name__ == '__main__':
    main()

