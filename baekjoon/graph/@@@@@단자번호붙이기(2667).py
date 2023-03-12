# x,y=q.poplef() >>> 배열이어도 각각으로 들어감
# 

'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

예제 출력 1 
3
7
8
9

'''

# bfs



from collections import deque

n=int(input())
map=[list(map(int,input())) for _ in range(n)]
cnt=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=[]


def bfs(map,x,y):
    global cnt
    cnt=1

    q=deque()
    q.append([x,y])
    map[x][y]=0

    while q:
        out_x, out_y = q.popleft()
        for i in range(4):
            x=out_x+dx[i]
            y=out_y+dy[i]

            if x <0 or x>=n or y <0 or y>=n:
                continue

            if map[x][y]==1:
                map[x][y]=0
                q.append([x,y])
                cnt+=1

    return cnt


for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col]==1:
            cnt=bfs(map,row,col)
            result.append(cnt)



result.sort()


print(len(result))
for i in result:
    print(i)



















# dfs

'''
n=int(input())
map=[list(map(int,input())) for _ in range(n)]
cnt=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=[]



def dfs(x,y):
    global cnt

    if x<0 or x >= n or y<0 or y>=n:
        return
    
    if map[x][y] == 1:
        map[x][y]=0
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx, ny)


for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col]==1:
            cnt=0
            dfs(row,col)
            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)




'''


