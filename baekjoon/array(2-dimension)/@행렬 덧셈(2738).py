# 리스트*상수는 그대로 곱해져서 한 리스트로 나옴
# [ ~ for _ in _ ] > 이거 자체가 이미 list이고 ~가 하나의 원소이다
# ~가 list이면 [ ] 속에 list가 들어간거지, 즉 for _ in _ 이 가로 덩어리(row)이고 ~가 그 안의 요소이다
# zip(list1, list2) >>> 각 요소들을 묶어 tuple들을 가진 zip객체를 만든다
# for x,y in zip() 많이 쓸 듯


'''
2.1. list comprehension 을 사용하기
[list1[i] + list2[i] for i in range(len(list1))]

2.2. zip 함수를 사용하기
[x+y for x,y in zip(list1, list2)]

'''


'''
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

예제 입력 1 
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

예제 출력 1 
4 4 4
6 6 6
5 6 100

'''

N, M = map(int, input().split())


A=[ list(map(int, input().split())) for row in range(N)]
B=[ list(map(int, input().split())) for row in range(N)]

# zip 노이용
'''
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j]+B[i][j], end=' ')
    print()
'''
# zip 이용
for i in range(len(A)):
    for x,y in zip(A[i], B[i]):
        print(x+y, end=' ')
    print()