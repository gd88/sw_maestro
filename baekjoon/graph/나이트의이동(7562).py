# 같은 곳에서 가는 최적의 경우의 수는 결국 하나다 >>> 고로 갔던 곳 갈 필요 x


'''
입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l * l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} * {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

예제 출력 1 
5
28
0

'''

from collections import deque

dy=[-1,-2,-2,-1,+1,+2,+2,+1]
dx=[-2,-1,+1,+2,-2,-1,+1,+2]

t=int(input())



def bfs():
    
    l=int(input())

    chess=[[0]*l for _ in range(l)]

    s=list(map(int, input().split()))
    f=list(map(int, input().split()))

    q=deque()
    
    chess[s[0]][s[1]]=0
    q.append([s[0],s[1]])

    
    while q:
        
        out_y, out_x=q.popleft()

        if out_y == f[0] and out_x ==f[1]:
            return print(chess[out_y][out_x])

        for i in range(8):
            y=out_y+dy[i]
            x=out_x+dx[i]

            if 0<=y<l and 0<=x<l and not chess[y][x]:
                q.append([y,x])
                chess[y][x]=chess[out_y][out_x]+1




for _ in range(t):
    bfs()
   





