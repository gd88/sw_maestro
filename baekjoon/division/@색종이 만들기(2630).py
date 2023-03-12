# 수틀리면 바로 재귀 해버리기
# return >>> @@함수@@를 나오는 것, braek >>> '반복문'을 나오는 것

'''
입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

예제 입력 1 
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

예제 출력 1 
9
7


'''


n=int(input())
paper=[ list(map(int, input().split()))  for _ in range(n)]

result=[]

# 첫째 색 확인, 나머지들과 비교 >>> 다르면 paper 재귀

# y,x는 네모 칸 중 첫째 자리

def sol(y,x,n):

    color=paper[y][x]

    for ty in range(y, y+n):
        for tx in range(x, x+n):
            # 수틀리면 바로 재귀 해버림
            if paper[ty][tx] != color:
                sol(y,x,n//2)
                sol(y+n//2,x,n//2)
                sol(y,x+n//2,n//2)
                sol(y+n//2,x+n//2,n//2)
                return
    
    if color == 0:
        result.append(color)
    else:
        result.append(color)


sol(0,0,n)

print(result.count(0))
print(result.count(1))







