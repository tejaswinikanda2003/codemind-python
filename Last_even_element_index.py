def fun(n):
    x = n
    for i in range(len(x)-1,-1,-1):
        if x[i] % 2 == 0:
            return i
y = int(input())
n = list(map(int,input().split()))
print(fun(n))