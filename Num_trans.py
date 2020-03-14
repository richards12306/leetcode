#!/usr/bin/python3

while True:
    number=int(input())
    dp=[]
    i=0
    while number!=0:
        dp.append(number%3)
        number=number//3

    dp.append(0)
    for i in range(len(dp)):
        if 2==dp[i]:
            dp[i]=-1
            dp[i+1]+=1
        elif 3==dp[i]:
            dp[i]=0
            dp[i+1]+=1
    dp=dp[::-1] if dp[-1]!=0 else dp[-2::-1]
    dp=list(map(str,dp))
    for i in range(len(dp)):
        if dp[i]=='-1':
            dp[i]='-'
    

    print(''.join(dp))

