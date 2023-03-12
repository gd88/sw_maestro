# 재귀함수 내 return 이 적어도 1이든 다른 영향이 없는 값이든 주어줘야 return이 올바르게 된다

'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력 1 
10

예제 출력 1 
3628800

'''

n=int(input())

def recur(x):

    if x==0:
        return 1
    if x==1:
        return 1
    
    return x*recur(x-1)


print(recur(n)) 
