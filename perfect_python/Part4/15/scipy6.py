import math

import numpy
from scipy import interpolate
import pylab


def main():

    xs = numpy.linspace(0, 2*math.pi, 9)
    ys = numpy.sin(xs)

    # (1) 今度は 0 から 2πまでの区間を 180 に句切った数列を作成
    xn = numpy.linspace(0, 2 * math.pi, 180)

    # (2) 元の数列を元にキュービック補間を用いて補間計算をする関数を生成
    f2 = interpolate.interp1d(xs, ys, kind='cubic')

    # 生成した関数を新しく作った数列に適用する
    yn = f2(xn)

    # 補間結果と元の結果をプロット
    # 詳細は Matplotlib の項へ
    pylab.plot(xs, ys, 'o-', xn, yn)
    pylab.show()


if __name__ == '__main__':
    main()
    
