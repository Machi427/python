#-*- coding:utf-8 -*-
import sys

import pygame
from pygame import display, image, time, key

DISPLAY_SIZE = (640, 480)


keymap = {}

def set_key_state(event):
    ''' キーの状態を保持する '''

    # キーの番号から名前に変換する
    name = key.name(event.key)

    # イベントの種類で 1 か 0 をセットする

    # キーが離されたイベント
    if event.type == pygame.KEYUP:
        keymap[name] = 0
    
    # キーが押されたイベント
    elif event.type == pygame.KEYDOWN:
        keymap[name] = 1


def get_key_state(name):
    '''キーの状態を取得する '''

    return keymap.get(name, 0)


def event_dispatch():
    '''
    ウィンドウのイベントを処理する
    '''

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # キー入力イベントを処理する
        elif event.type in {pygame.KEYDOWN, pygame.KEYUP}:
            set_key_state(event)


def main(argv=sys.argv[1:]):

    pygame.init()
    screen = display.set_mode(DISPLAY_SIZE)

    ball = image.load('samples/4-2/ball.png')

    # 描画座標を保持する変数
    x, y = 0, 0

    while True:
        event_dispatch()
        screen.fill((0, 0, 0))

        # 右矢印キーの入力状態と左矢印キーの入力状態を見て 1, 0, -1 の値を生成する
        dx = get_key_state('right') - get_key_state('left')

        # 下矢印キーの入力状態と上矢印キーの入力状態を見て 1, 0, -1 の値を生成する
        dy = get_key_state('down') - get_key_state('up')

        # キー入力状態から座標を変化させる
        x += dx * 5
        y += dy * 5

        # 変化させた座標に描画する
        screen.blit(ball, (x, y))

        display.flip()
        time.delay(100)


if __name__ == '__main__':
    main()
