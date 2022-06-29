def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
def avg(x):
    y=[]
    for k in x:
        if pn(k):
            y.append(k)
    s=sum(y)
    g=s/len(y)
    print(format(g, '.2f'))
n=int(input())
x=list(map(int,input().split()))
avg(x)