def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
def pl(x):
    d=0
    for k in x:
        if pn(k):
            if k<=m:
                d=d+1
    print(d)
n=int(input())
x=list(map(int,input().split()))
m=int(input())
pl(x)