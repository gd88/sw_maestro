# upper(), lower() 함수는 s=s.upper() 해줘야 한다
# set()은 중보글 지우고 unique하게 모으기 위해 사용한다
# s.count()는 갯수 찾기 


# 문자열만 find가능하다

# set()은 index가 안 되기에 list()로 다시 감싸야한다

'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi

예제 출력 1 
?

'''

S=input().upper()
unique_S=list(set(S))
# 갯수들 저장(숫자들만 저장, 그런데 앞에꺼부터 되겠지)
cnt_list=[]
for x in unique_S:
    cnt_list.append(S.count(x))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_S[cnt_list.index(max(cnt_list))])



