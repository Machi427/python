#-*- coding:utf-8 -*-
import sys

import pygame
from pygame import display, image, time

DISPLAY_SIZE = (640, 480)


def event_dispatch():
    '''
    ウィンドウのイベントを処理する
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def main(argv=sys.argv[1:]):

    pygame.init()
    screen = display.set_mode(DISPLAY_SIZE)

    # 画像を読み込む
    ball = image.load('samples/4-2/ball.png')

    while True:
        event_dispatch()
        screen.fill((0, 0, 0))

        # 読み込んだ画像をウィンドウの (0, 0) に表示する
        screen.blit(ball, (0, 0))

        display.flip()
        time.delay(100)


if __name__ == '__main__':
    main()

