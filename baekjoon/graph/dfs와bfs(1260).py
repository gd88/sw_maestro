# 출력할 때 정리를 하고 print 할지 코드 내려가면서 그때 그때 print할지

'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력 1 
1 2 4 3
1 2 3 4

'''


from collections import deque
import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline


n, m, r = map(int, input().split())

graph=[[] for _ in range(n+1)]
visited_1=[0]*(n+1)
visited_2=[0]*(n+1)


cnt=1


for _ in range(m):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    


def dfs(v):
    
    visited_1[v]=1
    print(v, end=' ')

    graph[v].sort()

    for i in graph[v]:
        if visited_1[i]==0:
            dfs(i)


def bfs(v):
    
    q=deque([r])
    visited_2[r]=1
    print(r, end=' ')

    while q:
        out=q.popleft()

        graph[out].sort()

        for i in graph[out]:
            if visited_2[i]==0:
                visited_2[i]=1
                q.append(i)
                print(i, end=' ')
        

dfs(r)
print()
bfs(r)
