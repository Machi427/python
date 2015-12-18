import png
import functools
import operator



def output_gen():
    ''' 出力用のデータ列を作る関数 '''

    result = []

    # 高さ分の繰り返し
    for y in range(256):

        # 一行分のデータの並び
        # データは以下のように r, g, b, の並びで一ピクセルを表現する
        # [r, g, b, r, g, b, ..., r, g, b]
        row = []

        # 幅の分の繰り返し
        for x in range(256):

            # R
            row.append(x)
            # G
            row.append(y)
            # B
            row.append(255-(x+y)//2)

        result.append(row)

    return result
    


def main():

    # 出力先ファイルオブジェクトを開く
    # バイナリモードにしなけれないけない
    fp = open('output2.png', 'wb')

    # Writer オブジェクトを作る
    # サイズは 256x で RGB 各要素のビット数は 8 に設定する 
    w = png.Writer(256, 256, bitdepth=8)

    # output_gen 関数の返値を出力する
    w.write(fp, output_gen())



if __name__ == '__main__':
    main()

