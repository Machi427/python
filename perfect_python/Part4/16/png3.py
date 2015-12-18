import sys
import png


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

    # 先程生成した output2.txt を読み込んだと仮定して

    # 画像の横幅(ピクセル数)
    print(width) #=> 256

    # 画像の高さ(ピクセル数)
    print(height) #=> 256

    # 画像のデータ(data は iterable なので一旦リストにする)
    buf = list(data)
    print(len(buf)) #=> 256

    # 画像の情報が辞書として返ってくる
    print(info) #=> {'alpha': False,
                #    'bitdepth': 8,
                #    'greyscale': False,
                #    'interlace': 0,
                #    'planes': 3,
                #    'size': (256, 256)}


if __name__ == '__main__':
    main()

