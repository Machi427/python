#-*- coding:utf-8 -*-
import sys

import pygame
from pygame import display, image, time, key

DISPLAY_SIZE = (640, 480)



def event_dispatch():
    '''
    ウィンドウのイベントを処理する
    '''

    for event in pygame.event.get():

        # 終了イベントであればプログラムを終了する
        if event.type == pygame.QUIT:
            sys.exit()


def main(argv=sys.argv[1:]):

    # pygame の初期化
    pygame.init()

    # サイズ 640x480 のウィンドウを生成する
    screen = display.set_mode(DISPLAY_SIZE)

    # プログラムの処理を行うループ
    while True:

        # ウィンドウを閉じるなどのイベント処理
        event_dispatch()

        # ウィンドウを黒で塗りつぶす
        screen.fill((0, 0, 0))

        # ディスプレイに色を反映させる
        display.flip()

        # 0.1秒待つ
        time.delay(100)


if __name__ == '__main__':
    main()

