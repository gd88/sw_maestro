'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1 
2

예제 출력 1 
1

'''

import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)


for i in range(1,n+1):
    if i==1:
        dp[i]=0
    else:
        if dp[i]%3==1:
            dp[i]=dp[i-1]+1
        elif dp[i]%3==2:
            dp[i]=dp[i//2]+1
        else:
            dp[i]=dp[i//3]+1

print(dp[n])













'''
cnt=0

while n != 1:
    if n % 3 == 1:
        n-=1
        cnt+=1
    elif n % 3 == 2:
        n=n//2
        cnt+=1
    else:
        n=n//3
        cnt+=1


print(cnt)

'''
