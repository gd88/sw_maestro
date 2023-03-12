# repalace(a,b) >>> a를 b로 대체
# 전체 갯수를 결국 세야하므로 array에 있는 요소들을 한 개짜리 문자로 대체시킨다


# 문자열은 count하고 index 알려주는 게 주력
# 삭제와 첨가 메소드는 없다

array=['c=', 'c-','dz=','d-','lj','nj','s=','z=']

word=input()

for x in array:
    if x in word:
        word=word.replace(x, 'a')
        

print(len(word))