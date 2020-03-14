#!/usr/bin/python3
#-*- coding=utf-8 -*-
while True:
    cou_kinds=int(input())
    for i in range(cou_kinds):
        cou_name,cou_day,cou_sec,cou_num=input().split( )

        cou_names=cou_names.append(cou_name[:-1])
        cou_nums=cou_nums.append(int(cou_num))
        cou_secs=cou_secs.append(cou_sec)
        cou_nums=cou_nums.append(cou_num)

    print("     +-----+-----------+-----------+-----------+-----------+-----------+ \n \
			    |     |    MON    |    TUE    |    WED    |    THU    |    FRI    | \n \
			    +-----+-----------+-----------+-----------+-----------+-----------+ \n \
			    |                          Morning                                | \n \
			    +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                |                                                                 | \n \
                +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                |                                                                 |   ")
    print("     +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                |                                                                 |  \n \
                +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                |                                                                 |   ") 
    print("     +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                |                         Afternoon                               | \n \
			    +-----+-----------+-----------+-----------+-----------+-----------+ \n \
                "
               )
    for i in range(4):
        for j in range(cou_kinds):
            if "Morning"==cou_secs[j]:
                