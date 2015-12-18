import sys
import os

import png


def to_pixels(data, channels=4):
    '''
    [r, g, b, r, g, b, ...] と並んでいると処理しづらいので
    [(r, g, b), (r, g, b)] チャンネル数ずつに句切ったタプルの列に直す
    '''
    buf = [0] * channels

    for line in data:
    
        try:
            it = iter(line)

            while True:

                for i in range(channels):

                    buf[i] = next(it)

                yield tuple(buf)

        except StopIteration:
            pass



def mosaic(data, width, height, channels, mosaic_w=16, mosaic_h=16):
    '''
    モザイクをかけてみる
    色のフォーマットは RGB のみ対応
    '''

    result = []

    # タプルのリストに変換
    pixels = list(to_pixels(data, channels))


    for y in range(height):

        line = []
        
        for x in range(width):

            m_x = x // mosaic_w * mosaic_w
            m_y = y // mosaic_h * mosaic_h

            # 現在の位置にあるピクセルではなく
            # mosaic_w, mosaic_h で句切った範囲を
            # 範囲の左上のピクセルと同色で塗りつぶす
            line.extend(pixels[m_x + m_y * width])

        result.append(line)

    return result



def write(fname, data, info):
    '''
    書き込む
    '''

    with open(fname, 'wb') as fp:

        # ファイルから読み込んだ情報をそのまま出力する
        w = png.Writer(**info)

        w.write(fp, data)


def gen_output_name(fname):
    ''' 出力ファイル名を生成 '''

    name, ext = os.path.splitext(fname)

    return name + '_mosaic' + ext


def main(argv=sys.argv[1:]):

    if len(argv) < 1:
        print('ファイル名を入力してください', file=sys.stderr)
        return

    # コマンドラインオプションの一つ目をファイルパスとして使う
    fpath = argv[0]

    # ファイルパスを渡して Reader クラスのインスタンスを作成
    reader = png.Reader(fpath)

    # 実際に読み込む
    # 結果が4要素のタプルで返ってくるので、適宜受け取る
    width, height, data, info = reader.read()

    # チャンネル数
    channels = info['planes']

    # モザイク処理
    data = mosaic(data, width, height, channels)

    # 出力ファイル名生成
    outputname = gen_output_name(fpath)

    # 書き出し
    write(outputname, data, info)
    

if __name__ == '__main__':
    main()

