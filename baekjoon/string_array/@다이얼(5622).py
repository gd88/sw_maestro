# 문자열에 요소가 있는지 확인하기 위해 in 사용
# @@index를 모르고 값만 알더라도 index()를 사용하면 알 수 있다!!!

words=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ' ]

word=input()
t=0


for i in word:
    for j in range(len(words)):
        if i in words[j]:
            t+=j+3


print(t)

