# 한 팀 인원만 구하면 남은 팀 구할 수 있다

'''
입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. 
Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

예제 출력 1 
0

'''


n=int(input())
s=[ list(map(int, input().split()))  for _ in range(n)]

a_member=[]
res=[]


def dfs(start):

    # 인원차면 비교
    if len(a_member) == n//2:
        b_member=[]
        for i in range(n):
            if i not in a_member:
                b_member.append(i)

        a_skill=0
        b_skill=0

        for i in range(n//2-1):
            for j in range(i+1,n//2):
                a_skill+=s[a_member[i]][a_member[j]]+s[a_member[j]][a_member[i]]
        
        for i in range(n//2-1):
            for j in range(i+1,n//2):
                b_skill+=s[b_member[i]][b_member[j]]+s[b_member[j]][b_member[i]]

        res.append(abs(a_skill-b_skill))
        return
        

    
    for i in range(start,n):
        a_member.append(i)
        dfs(i+1)
        a_member.pop()






dfs(0)

print(min(res))


