#!/usr/bin/python3
# -*- coding: UTF-8 -*-
def quick_algorithm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans


lst = []
while(True):

    a,b,c = list(map(int,input().split()))
    if(a==0):
        break
    print(quick_algorithm(a,b,c))