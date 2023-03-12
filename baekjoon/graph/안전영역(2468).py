'''
입력
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

출력
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

예제 입력 1 
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

예제 출력 1 
5

예제 입력 2 
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

예제 출력 2 
6

'''

# 비가 내리는 수치를 정하고 visited에 1처리한다 >> 구역을 bfs로 찾는다
# 위에 것들을 비가 내리는 수치들을 점차 증가시키면서 파악


from collections import deque

n=int(input())


city=[ list(map(int, input().split())) for _ in range(n)]

res=[]

max_height=0

dy=[-1,1,0,0]
dx=[0,0,-1,1]



def bfs(y,x):
    q=deque()
    q.append([y,x])
    visited[y][x]=0

    while q:
        out_y, out_X=q.popleft()

        for i in range(4):
            y=out_y+dy[i]
            x=out_X+dx[i]
            if y<0 or y>=n or x<0 or x>=n:
                continue
            if visited[y][x] == 0:
                visited[y][x]=1
                q.append([y,x])










for i in city:
    for j in i:
        if j > max_height:
            max_height=j

# 비 수치
for i in range(max_height+1):
    # 물 찬 곳들 visited에 1처리
    visited=[[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if city[j][k] <= i:
                visited[j][k]=1
    cnt=0
    # bfs로 구역 개수 확인
    for j in range(n):
        for k in range(n): 
            if visited[j][k]==0:
                bfs(j,k)
                cnt+=1
    
    res.append(cnt)


print(max(res))


