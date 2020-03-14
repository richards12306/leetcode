#!/usr/bin/python3
# -*- coding: UTF-8 -*-
Num,interger=list(map(int,input().split( )))
label=0
for i in range(Num):
    label+=1
    while str(interger) in str(label):
        label+=1
    Max=label
    
print(label)

#include<stdio.h>
int main(){
    int n,i,j,res=0;
    scanf("%d",&n);
    for(i=0;i<2*n+1;i++){
        scanf("%d",&j);
        res=j^res;
    }
    printf("%d\n",res);
    return 0;  
}


}


