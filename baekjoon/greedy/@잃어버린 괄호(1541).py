# 그리디인진 모르겠지만 적당한 구현력 문제

# - 기준으로 괄호치면된다.
# 그리고 구분된 것 내부들은 다 더하고 남은 것들은 다 뺴버린다 

# split()은 영구반영 안 돼서 = 해야한다
'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 '0'~'9', '+', 그리고 '-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1
55-50+40

예제 출력 1 
-35

'''



# - 기준으로 짜르기, list 형태 된다
expression=input().split('-')

# 리스트 내부에는 +가 있거나 그냥 수 하나이므로 +있는 것은 더해 버리기
for i in range(len(expression)):
    expression[i]=expression[i].split('+')
    sum=0
    
    for j in range(len(expression[i])):
        sum+=int(expression[i][j])
    
    expression[i]=sum

answer=expression[0]

for i in range(1, len(expression)):
    answer-=expression[i]

print(answer)