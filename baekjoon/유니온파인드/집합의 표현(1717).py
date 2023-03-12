'''
예제 입력 1 
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

예제 출력 1 
NO
NO
YES

'''
# 함수의 역할과 return해야할 것들 써놓기 >> 메인 코드 짜면서 필요한 위치에 함수 넣어보기, 이 때 어떤 파라미터가 필요한지 알 수 있다.


# c가 0이면 합치기 > 아니면 부모 find하기
# 가장 상위 부모노드는 자기자신을 부모노드로 가진다

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int, input().split())
# 초기: 자기 자신을 부모로 가지는 부모집합
parent=[i for i in range(n+1)]

# 부모를 찾는 함수
def find_parent(x):

    if parent[x]==x:
        return x
    else:
        return find_parent(parent[x])




# 부모를 연결지어 합집합으로 만드는 함수    
def union_parent(a,b):
    # 부모노드를 타고 올라가 가장 작은 부모노드에 연결짓는다
    # 부모노드 찾기
    a=find_parent(a)
    b=find_parent(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b


for i in range(m):
    c,a,b=map(int, input().split())
    # union 경우    
    if c==0:
        union_parent(a,b)
    else:
        if find_parent(a)==find_parent(b):
            print('YES')
        else:
            print('NO')
        

