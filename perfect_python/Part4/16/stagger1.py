#-*- coding:utf-8 -*-

import sys
import os

import stagger
from stagger import id3


def main(args=sys.argv[1:]):

    fpath = args[0]

    # stagger.read_tag 関数で mp3 ファイルからタグ情報を読み込む
    tag = stagger.read_tag(fpath)

    print(tag) #=>e<Tag23: ID3v2.3 tag with 11 frames> など

    # ID3 タグに記録されたタイトルを取得
    print(tag.title)

    # ID3 タグに記録されたアルバム名を取得
    print(tag.album)



if __name__ == '__main__':
    main()

