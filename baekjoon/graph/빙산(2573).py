'''
입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. 
N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 
각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력 1 
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

예제 출력 1 
2

'''

# 숫자를 찾는다 > 동서남북 방향을 찾고 갯수를 모두 측정한 이후에 줄인다
from collections import deque

n,m=map(int, input().split())

glacier=[list(map(int, input().split()))  for _ in range(n)]




dy=[-1,1,0,0]
dx=[0,0,-1,1]



def bfs(y,x):
    global glacier

    visited=[[0]*m for _ in range(n)]
    melt=[]

    q=deque()
    q.append([y,x])
    visited[y][x]=1


    while q:
        out_y, out_x= q.popleft()
        cnt=0

        for i in range(4):
            y=out_y+dy[i]
            x=out_x+dx[i]
            if y<0 or y>=n or x<0 or x>=m:
                continue
            if visited[y][x]==0:            
                q.append([y,x])
                visited[y][x]=1

            if glacier[y][x]==0:
                cnt+=1
            
        melt.append([out_y,out_x,cnt])

    
    for y,x,cnt in melt:
        if glacier[y][x] <= cnt:
            glacier[y][x]=0
        else:
            glacier[y][x]-=cnt

    return 1




check=1

        
step=0
while check :
    step+=1
    # 한 단계
    div=0
    for i in range(n):
        for j in range(m):
            if glacier[i][j]!=0:
                # bfs 한 번 할 때 연결된 거 모두 감소한 것과 +1 방출
                div+=bfs(i,j)
                print(glacier)
            
    print(div)
    if div == 2:
        print(step)

    check=0        
    for g in glacier:
        check+=sum(g)


