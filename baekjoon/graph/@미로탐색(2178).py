# 뭔가 겹치는 오는 장소에서 늦게 온 길이 맞는 데라고 생각할 수도 있는데 그 겹치는 장소가 애초에 맞다면 먼저 온 것도 맞기에 빠른 것이 비교 안 해도 된다
# 1인 경우만 생각


'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011

예제 출력 1 
15

예제 입력 2 
4 6
110110
110110
111111
111101

예제 출력 2 
9

'''

from collections import deque

n, m = map(int, input().split())
maze=[ list(map(int,input())) for row in range(n)]


dx=[0,0,-1,1]
dy=[-1,1,0,0]


def bfs():

    maze[0][0]=1
    q=deque()
    q.append([0,0])

    while q:

        out_y, out_x = q.popleft()
        
        
        for i in range(4):
            y=out_y+dy[i]
            x=out_x+dx[i]

            if x <0 or x >= m or y <0 or y >=n:
                continue

            if maze[y][x] ==1:
                q.append([y,x])
                maze[y][x]=maze[out_y][out_x]+1

            

            


bfs()

print(maze[n-1][m-1])







