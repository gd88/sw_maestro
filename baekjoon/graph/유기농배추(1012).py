'''
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

예제 출력 1 
5
1

예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

예제 출력 2 
2


'''


import sys
input=sys.stdin.readline
from collections import deque


sys.setrecursionlimit(10**6)


# bfs


def bfs(y,x):
    q=deque()

    maps[y][x]=0
    q.append([y,x])

    while q:
        out_y, out_x = q.popleft()

        for i in range(4):
            x=out_x+dx[i]
            y=out_y+dy[i]

            if 0 <= x <m and 0<= y <n:
                if maps[y][x]==1:
                    maps[y][x]=0
                    q.append([y,x]) 








t=int(input())
result=[0]*t

dx=[0,0,-1,1]
dy=[-1,1,0,0]


for i in range(t):
    
    m,n,k=map(int, input().split())
    maps=[ [0]*m for row in range(n)]

    for _ in range(k):
        x,y=map(int, input().split())
        maps[y][x]=1

    for row in range(n):
        for col in range(m):
            if maps[row][col] == 1:
                bfs(row,col)
                result[i]+=1




for i in result:
    print(i)










# dfs

'''
def dfs(y,x):
    maps[y][x]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if maps[ny][nx] == 1:
            dfs(ny,nx)



t=int(input())
result=[0]*t

dx=[0,0,-1,1]
dy=[-1,1,0,0]


for i in range(t):
    
    m,n,k=map(int, input().split())
    maps=[ [0]*m for row in range(n)]

    for _ in range(k):
        x,y=map(int, input().split())
        maps[y][x]=1

    for row in range(n):
        for col in range(m):
            if maps[row][col] == 1:
                dfs(row,col)
                result[i]+=1


for i in result:
    print(i)


'''