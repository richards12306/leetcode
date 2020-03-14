#!/usr/bin/python3
#-*- coding=utf-8 -*-

while True:
    n=input()
    if n=="EOF":
        break
    else:
        n=int(n)
    print(int((n**3+5*n)/6+1))
    
#include<stdio.h>
#include<math.h>
 
int main()
{
    long long n;
    long long max;
    while(scanf("%lld",&n)!=EOF)
    {
        max=(n*n*n+5*n+6)/6;
        printf("%lld\n",max);
        }
    return 0;
}
