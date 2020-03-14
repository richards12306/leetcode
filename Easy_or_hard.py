#!/usr/bin/python3
#-*- coding=utf-8 -*-
name_num = int(input())
for i in range(name_num):
    name = input().split( )
    print('{} {}'.format(name[1],name[0]))
    


#include<stdio.h>
#include<string.h>
int main(){
    int i,t,j,l,n;
    scanf("%d",&t);
    char name[2][200];
    for(i=0;i<t;i++){
    	scanf("%s %s",&name[0],&name[1]);
    	for(j=0;j<2;j++){
    		l=strlen(name[j]);
    		n=0;
    		while(n<l){
    			if((n==0)&&(name[j][0]>='a')&&(name[j][0]<='z'))
    			name[j][0]-=32;
    			else if((n>0)&&(name[j][n]>='A')&&(name[j][n]<='Z'))
				name[j][n]+=32;
				n++;
			}
		}
		printf("%s %s\n",name[1],name[0]);
	}
	return 0;
}
