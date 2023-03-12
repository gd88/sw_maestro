'''
예제 입력 1 
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

예제 출력 1 
3

'''

n=int(input())
electric=[list(map(int, input().split())) for _ in range(n)]
electric.sort(key=lambda x:x[0])

cnt=0


dp=[0]*n




for i in range(n):
    for j in range(i):
        if electric[i][1] > electric[j][1] and dp[i]<dp[j]:
            dp[i]=dp[j]
    
    dp[i]+=1

print(n-max(dp))
