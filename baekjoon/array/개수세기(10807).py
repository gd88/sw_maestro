# input()은 문자열
# split()은 ()안의 구분자를 기준으로 자른다
# input().split() 은 input()으로 받고 공백을 기준으로 잘라 list로 만든다. 그래서 띄어쓰기로 각각 저장되는 거다 # a,b =input().split()
# N,X=list(map(int,input().split()))도 되고 N,X=map(int,input().split())

# map(f, iterable한 자료형) # 우측을 function에 집어넣어 map 객체를 반환다 # 그래서 보통 list나 tuple을 덮어씌운다
# list(map(int, input().split())
# int()함수는 list를 int로 바꾸어 줄 수 없기에 int(input().split())은 안 된다
# array.count(object) >>> array에서 object와 같은 값을 가지는 개수를 반환한다

'''
문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

'''


N=int(input())
N_list=list(map(int, input().split()))
v=int(input())

print(N_list.count(v))

