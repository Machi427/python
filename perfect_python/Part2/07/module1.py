#!/bin/env python
# -*- coding: utf-8 -*-

"""
これは mymodule.py のドキュメンテーション文字列です。
このモジュールは、一般的なモジュールの作成方法を示すサンプルです。
"""

SPAM = "spam"

def ham(arg):
    print(arg)

class Egg:
    pass

if __name__ == '__main__':
    ham(Egg())

