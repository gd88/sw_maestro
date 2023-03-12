# for 같은 건 >>> 이건 무슨 목적, 효과, 행위를 위해 넣었을 수 밖에 없었을까를 생각
# dfs : 방문찍고 (visited=count) 어느 다음 정점으로 옮길지 for로 찾고 다음 정정으로 넘어감 (dfs(다음 정점))
# graph = 노드와 간선들을 2중 리스트로 나타냈다 # visited = 노드들의 방문순서(방문check)이며 count를 이용한다, 처음엔 0으로 초기화

# input=sys.stdin.readline  >>> input 이랑 같은 기능인데 시간 단축
# sys.setrecursionlimit(10**6)  >>> python은 재귀의 최대 깊이를 1000로 제한하므로 이렇게 늘려준다, 안 그럼 런타임에러 난다



'''
문제
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}

입력
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. 
(1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

출력
첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 
시작 정점에서 방문할 수 없는 경우 0을 출력한다.

예제 입력 1 
5 5 1
1 4
1 2
2 3
2 4
3 4

예제 출력 1 
1
2
3
4
0

'''

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)



n, m, r = map(int, input().split())

graph=[ [] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=1

# graph에 간선 부여
for _ in range(m):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# dfs(r) >>> visited에 있는 r자리에 count 부여하고 graph[r] 에 있는 요소들 오름차순 정렬 가지 않은 간선(vistied이 0인 간선)을 찾고 dfs(r)로 뿅

def dfs(n):
    global cnt
    visited[n]=cnt
    graph[n].sort()
    # for >>> 이미 갔던 간선인지 확인하는 작업
    for u in graph[n]:
        # 어라, 안 간 곳이네
        if visited[u] == 0:
            cnt+=1
            # cnt 증가시키고 dfs 이동, 거기서 visited 부여
            dfs(u)

dfs(r)

for i in range(1, n+1):
    print(visited[i])


# 흘려보냄이 없다. 미학적으로 훌륭하다