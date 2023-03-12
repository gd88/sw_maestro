# 예외도 사다리 전도 +1 해줘야 한다 하


'''
입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

예제 입력 1 
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

예제 출력 1 
3

예제 입력 2 
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21

예제 출력 2 
5



'''

from collections import deque


d=[1,2,3,4,5,6]

n,m=map(int, input().split())


board=[0]*101
s1=[]
s2=[]


for _ in range(n+m):
    x,y=map(int, input().split())
    s1.append(x)
    s2.append(y)




def bfs():


    q=deque()
    q.append(1)

    while q:

        out=q.popleft()

        if out==100:
            print(board[out])
            return

        for i in range(6):
            x=out+d[i]

            if x <= 0 or x >= 101:
                continue

            if not board[x]:
                if x in s1:
                    f=s1.index(x)
                    board[s2[f]]=board[out]+1
                    board[x]=board[out]+1
                    q.append(s2[f])
                else: 
                    board[x]=board[out]+1
                    q.append(x)



            



bfs()






