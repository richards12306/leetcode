#!/usr/bin/python3
# -*- coding: UTF-8 -*-
while True:
    peoples_nums=int(input())
    id_numbers=[]
    namess=[]
    dicts={}
    for i in range(peoples_nums):
        id_number,names=input().split( )
        id_number=int(id_number)
        dicts[id_number]=names
        # id_numbers.append(id_number)
        # namess.append(names)
    sets_num=int(input())
    for i in range(sets_num):
        query_num=int(input())
        comparablities=0
        for j in range(query_num):
            id_a,id_b=list(map(int,input().split( )))
            string_a=dicts[id_a]
            string_b=dicts[id_b]
            mix_len=len(string_b) if len(string_b)<len(string_a) else len(string_a)
            for i in range(mix_len):
                if string_a[i]!=string_b[i]:
                    comparablities=comparablities+i
                    break

        print(comparablities)

