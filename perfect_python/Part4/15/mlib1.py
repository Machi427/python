import math

import numpy
from matplotlib import pyplot


def make_rotate_matrix(rad):

    return numpy.array([[math.cos(rad), -math.sin(rad)],
                        [math.sin(rad), math.cos(rad)]]).transpose()


def main():

    num = 20

    print('degree \t result')

    # 計算結果の保持用
    x_positions = []
    y_positions = []

    base = numpy.array([1, 0])

    for x in range(num+1):

        rad = x * math.pi * 2 / num

        rot = make_rotate_matrix(rad)
        deg = 360 / num * x

        result = numpy.dot(base, rot)

        print(deg, '\t', result)

        # 保存しておく
        x_positions.append(result[0])
        y_positions.append(result[1])

    # プロットする
    pyplot.plot(x_positions, y_positions)

    # y 軸のラベルを設定
    pyplot.ylabel('Y-axis')

    # x 軸のラベルを設定
    pyplot.xlabel('X-axis')

    # UI とともに描画
    pyplot.show()


if __name__ == '__main__':
    main()

