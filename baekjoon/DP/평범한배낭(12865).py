'''
예제 입력 1 
4 7
6 13
4 8
3 6
5 12

예제 출력 1 
14
'''



n,k=map(int, input().split())
arr=[ list(map(int, input().split())) for _ in range(n)]
dp=[ [0,0] for _ in range(n)]



for i in range(n):
    if arr[i][0]<=k:
        dp[i][0]=arr[i][0]
        dp[i][1]=arr[i][1]
        for j in range(i):     
            if dp[j][0]+arr[i][0] <=k :
                if dp[i][1] < dp[j][1]+arr[i][1]:
                    dp[i][1] = dp[j][1]+arr[i][1]
                    dp[i][0] = dp[j][0]+arr[i][0]
                    

max=0
for i in range(n):
    if max < dp[i][1]:
        max=dp[i][1]

print(max)           







