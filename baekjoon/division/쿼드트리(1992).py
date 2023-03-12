'''
입력
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. 
N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 
각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

출력
영상을 압축한 결과를 출력한다.

예제 입력 1 
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

예제 출력 1 
((110(0101))(0010)1(0001))

'''



n=int(input())
paper = [ list(map(int, input())) for _ in range(n) ]


def dfs(y,x,n):


    color=paper[y][x]

    for i in range(y,y+n):
        for j in range(x,x+n):
            if paper[i][j] != color:
                print('(', end='')
                dfs(y,x,n//2)
                dfs(y,x+n//2,n//2)
                dfs(y+n//2,x,n//2)
                dfs(y+n//2,x+n//2,n//2)
                print(')', end='')
                return

    return print(color,end='')



dfs(0,0,n)
                




