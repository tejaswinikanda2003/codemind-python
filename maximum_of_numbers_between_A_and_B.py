n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
v=[]
for i in x:
    if i>n and i<=m:
        v.append(i)
if len(v):
    print(max(v))
else:
    print("-1")
    