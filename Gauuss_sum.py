#!/usr/bin/python3
#-*- coding=utf-8 -*-
num = int(input())
for i in range(num):
    start, end = list(map(int,input().split( )))
    result = int((start+end)*(end-start+1)//2)
    print('Case #{}: {}'.format(i+1,result))