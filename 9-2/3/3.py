def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>=2:
        return f(n-1)+f(n-2)


n=int(input())
print(f(n))