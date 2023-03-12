# 재귀에 대한 개념 총망라

# if를 수직으로 배치하면 if를 단계 별로 탐험시킬 수 있다


# r을 따로 지정해버리면 재귀에서 돌아올 때 이전 값으로 가질 않는다. 재귀와 함께 돌아오려면 인수로 받자
# operator도 마찬가지이다. 감소했던 값을 다시 늘리려면 인수로 받아야 한다
# n개의 결과값인 answer도 마찬가지....

# 음수 몫 계산

'''
입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. 
(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(*)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

예제 입력 1 
2
5 6
0 0 1 0

예제 출력 1 
30
30

예제 입력 2 
3
3 4 5
1 0 1 0

예제 출력 2 
35
17

예제 입력 3 
6
1 2 3 4 5 6
2 1 1 1

예제 출력 3 
54
-24

'''




n=int(input())
numbers=list(map(int, input().split())) 
operator=list(map(int, input().split())) # n-1개의 자리에 들어간다


result=[]


def dfs(depth, answer, plus, minus, multiple, divide):
    

    if depth==n-1:
        result.append(answer)
        return



    if plus:
        dfs(depth+1, answer+numbers[depth+1], plus-1, minus, multiple, divide)

    if minus:
        dfs(depth+1, answer-numbers[depth+1], plus, minus-1, multiple, divide)
    
    if multiple:
        dfs(depth+1, answer*numbers[depth+1], plus, minus, multiple-1, divide)

    if divide:
        dfs(depth+1, int(answer/numbers[depth+1]), plus, minus, multiple, divide-1)


dfs( 0, numbers[0], operator[0], operator[1], operator[2], operator[3])

print(max(result))
print(min(result))