# deque에 넣는다 >> 넣은 index에 맞는 visited에 cnt 부여 >> (while 시작) deque에서 뱉는다 >> 뱉은 index에 맞는 graph에 오름차순 정렬 
# >> 안 간 index들 deque에 넣는다 >> 넣은 index에 맞는 visited에 cnt 부여 (deque와)

# dfs에서는 graph를 이용해 다음 목적지를 확인, graph의 같은 [ ]에 있더라도 방문순서가 아예 동떨어질 수 있기때문
# bfs는 deque에 들어간 순서대로 방문이므로 visited에 cnt를 바로 부여, graph의 같은 [ ]에 있으면 방문순서가 바로 옆이다
# deque는 popleft 등을 이용해 왼쪽에서 뺄 수 있다(list는 무조건 오른쪽에서 빼고 넣음)

# bfs는 재귀가 아니다, while문 사용
# 함수 밖에서 선언한 변수는 함수 내에서도 사용 가능, 그런데 값을 변경할 수는 없다, 그래서 안에서 global을 붙여버림
# 함수 내에서 선언한 변수를 밖에서 사용하려면 global 변수로 만든다



'''
문제
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}

입력
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

출력
첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

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
4
3
0

'''
from collections import deque
import sys
input=sys.stdin.readline


n,m,r=map(int, input().split())

visited=[0]*(n+1)
graph=[ []  for _ in range(n+1)]


for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt=1

def bfs():

    global cnt
    
    q=deque()
    q.append(r)
    visited[r]=cnt

    while q:
        out=q.popleft()


        graph[out].sort()

        for i in graph[out]:
            if visited[i]==0:
                cnt+=1
                q.append(i)
                visited[i]=cnt
                


bfs()

for i in visited[1::]:
    print(i)

    



    









