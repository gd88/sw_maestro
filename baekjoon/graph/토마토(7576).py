'''
입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. 
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1 
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

예제 출력 1 
8

예제 입력 2 
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

예제 출력 2 
-1

예제 입력 3 
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

예제 출력 3 
6


'''

# 다 하고 0있으면 그건 못하는 거
# 퍼져갈수록 1씩 증가   # 가장 큰 값이 답
# 0이면 이동


from collections import deque
import sys
input=sys.stdin.readline

m,n=map(int, input().split())
tomato=[list(map(int, input().split())) for _ in range(n)]

dy=[1,-1,0,0]
dx=[0,0,-1,1]


def bfs():
    
    q=deque()
    
    # 처음부터 1인 것들을 동시에 q에 넣어야 한다
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                q.append([i,j])

    while q:

        out_y, out_x = q.popleft()
        
        for i in range(4):
            y=out_y+dy[i]
            x=out_x+dx[i]

            if y < 0 or x < 0 or y >= n or x >= m: 
                continue
            
            if tomato[y][x] == 0:
                q.append([y,x])
                tomato[y][x]=tomato[out_y][out_x]+1




bfs()

res=0

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)

