def fact(k):
    m=1
    for j in range(1,k+1):
        m=m*j
    return m
n=int(input())
for i in range(n):
    s=0
    a=int(input())
    s=s+fact(a)
    print(s)