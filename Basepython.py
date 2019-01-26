#!/usr/bin/python
# -*- coding: UTF-8 -*-

arr = ['app','bpp','cpp','dpp']
for i in arr:
    if i.startswith('b'):
        print('i: ',i)
        print('arr[1]: ', arr[1])
        print('found')
        break;
else:
    print('Not Found')

