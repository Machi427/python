# -*- coding:utf-8 -*-

with open('test.txt') as f:
    search = input()
    count = 0
    for line in f:
        if line.indexof(search) > -1:
            count += 1
    print(count)
