#!/usr/bin/python3
# -*- coding: UTF-8 -*-array.sort()

array=input().split( )
for i in range(len(array)):
    array[i]=int(array[i])
array = list(set(array))
array.sort(reverse=False)
for i in array[1:]:
    print(i,end=' ')
