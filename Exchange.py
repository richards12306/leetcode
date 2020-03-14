#!/usr/bin/python3
# -*- coding: UTF-8 -*-

while True:
    num =int(input())
    if 0 == num:
        break
    in_array =input().split( )
    in_array=list(map(int,in_array))
    ans=0
    for i in range(len(in_array)):
        for k in range(len(in_array)-i-1):
            if in_array[k]>in_array[k+1]:
                t=in_array[k]
                in_array[k]=in_array[k+1]
                in_array[k+1]=t
                ans+=1
    print(ans)

    # dicts={}
    # points=point=0
    # for i in range(len(in_array)):
    #     dic[i+1]=in_array[i]
    #     point=i+1-in_array[i] if i+1>in_array[i] else in_array[i]-i-1
    #     points=points+point
    # print(int(points/2))
    # nums=0
    # for i in range(1,len(dicts)+1):
    #     if i in dicts:
    #         if i == dicts[i]:
    #             dicts.pop(i)
    #             nums+=1
    #         else: 
    #             while True:
    #                 i=dicts[i]
    #                 dicts.pop(i)
    #                 if i not in dicts:
    #                     nums+=1
    #                     break
    # print(num-nums)


