def soe(x):
    y=[]
    for i in x:
        if i<n or i>m:
            y.append(i)
    if len(y)!=0:
        print(*y)
    else:
        print("-1")
n=int(input())
x=list(map(int,input().split()))
#print(x)
n,m=map(int,input().split())
#print(n,m)
soe(x)
