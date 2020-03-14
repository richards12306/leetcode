#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#0/1背包问题
#构造一个背包函数，
# def Values(kinds,nums):
#     if kinds==0:
#         return 0 

#     remain_nums=nums-anaimals[kinds-1][0]
#     if remain_nums>=0:
#         token_value=Values(kinds-1,remain_nums)+anaimals[kinds-1][1]
#         untoken_value=Values(kinds-1,remain_nums)
#         token= token_value if token_value>untoken_value else untoken_value 
#         return token
#     else:
#         remain_nums=nums
#         untoken_value=Values(kinds-1,remain_nums)
#         return untoken_value



# while True:
#     nums=[]
#     points=[]
#     kinds=int(input())
#     for i in range(kinds):
#         num,point=input().dplit( )
       
#         nums.append(int(num))
#         points.append(int(point))
#     max_size=int(input())
#     dp=[]
#     for i in range(100005):
#         dp.append(0)
#     for i in range(kinds):
#         for j in range(max_size,0,-1):
#             if j<nums[i]:
#                 break
#             else:
#                 dp[j]=max([ dp[j],dp[j-nums[i]]+points[i] ])
        

#     print(dp[max_size])


#include<iostream>
#include<string.h>
using namedpace std;

int dp[100005];//dp[v]表示背包大小为v时候的最优解
int main()
{
    int n,k;
    int dp[105],w[105];
    while(cin>>n)
    {
        for(int i=0;i<n;i++)
        {
            cin>>dp[i]>>w[i];
        }
        cin>>v;
        for(int i=0;i<=k;i++)dp[i]=0;        
        for(int i=0;i<n;i++)
        {

            for(int j=k;j>=dp[i];j--)
            {
                dp[j]=max(dp[j],dp[j-dp[i]]+w[i]);
            }
        }
        cout<<dp[k]<<endl;
    }
}





    # sorted_anaimals=sorted(anaimals.items(),key=lambda i:i[1][1],reverse=True)
    # Max_point=0
    # Max_point=Values(kinds,max_size)
    # print(Max_point)



