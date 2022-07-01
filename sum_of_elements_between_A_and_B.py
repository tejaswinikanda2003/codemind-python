n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
c=[]
for i in x:
    if i>=n and i<=m:
        c.append(i)
if len(c)!=0:
    print(sum(c))