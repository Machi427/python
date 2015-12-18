#-*- coding:utf-8 -*-

import sys
import os

import stagger
from stagger import id3


def main(args=sys.argv[1:]):

    fpath = args[0]

    tag = stagger.read_tag(fpath)

    # タイトルを変更する
    tag.title = 'motto☆派手にね!'

    # アーティストを変更する
    tag.title = '戸松遥'

    # 同じファイルにタグ情報を書き出す
    tag.write()



if __name__ == '__main__':
    main()

