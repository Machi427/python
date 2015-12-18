import numpy
import math


def make_rotate_matrix(rad):
    ''' 回転行列を生成する '''
    return numpy.array([[math.cos(rad), -math.sin(rad)],
                        [math.sin(rad), math.cos(rad)]]).transpose()


def main():
    
    num = 20

    # (1, 0) という向きのベクトル
    base = numpy.array([1, 0])

    print('degree \t result')

    for x in range(num+1):

        # 回転させる角度をラジアンで計算
        rad = x * math.pi * 2 / num

        # 回転行列を生成
        rot = make_rotate_matrix(rad)

        # 表示用に度を計算
        deg = 360 / num * x

        # numpy.dot を使って回転させる
        result = numpy.dot(base, rot)

        # 結果の出力
        print(deg, '\t', result)
 

if __name__ == '__main__':
    main():

