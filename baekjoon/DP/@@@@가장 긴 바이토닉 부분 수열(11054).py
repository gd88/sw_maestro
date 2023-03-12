'''
예제 입력 1 
10
1 5 2 1 4 3 4 5 2 1

예제 출력 1 
7

'''



n=int(input())
arr_1=list(map(int, input().split()))
arr_2=arr_1[::-1]


dp_1=[0]*n
dp_2=[0]*n


for i in range(n):
    for j in range(i):
        if arr_1[i] > arr_1[j] and dp_1[i] < dp_1[j]:
            dp_1[i]=dp_1[j]
    dp_1[i]+=1

for i in range(n):
    for j in range(i):
        if arr_2[i] > arr_2[j] and dp_2[i] < dp_2[j]:
            dp_2[i]=dp_2[j]
    dp_2[i]+=1

dp_2=dp_2[::-1]


dp_3=[]
for i in range(n):
    dp_3.append(dp_1[i]+dp_2[i])



print(max(dp_3)-1)
