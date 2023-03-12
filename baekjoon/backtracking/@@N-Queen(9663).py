# 기본 back과 원리는 같다
# is_promising이라는 함수를 추가시켜 확인작업
# x가 행 i가 열
# abs(chess[i]-chess[x]) == abs(i-x) >>> 테크닉

# 쭉 뻗은 대각선 상화좌우 다 된다

'''
문제
N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92

'''






n=int(input())
chess=[0]*n
result=0

def is_promising(x):
    # 위쪽과 같은 열
    for i in range(x):
        if chess[i] == chess[x] or abs(chess[i]-chess[x]) == abs(i-x): 
            return 0
        
    return 1



# x는 행을 의미
def queens(x):
    global result

    if x==n:
        result+=1
        return

    for i in range(n):
        chess[x]=i
        if is_promising(x):
            queens(x+1)


queens(0)


print(result)







