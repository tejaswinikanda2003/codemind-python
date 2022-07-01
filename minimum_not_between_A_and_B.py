n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
v=[]
for i in x:
    if i<n or i>m:
        v.append(i)
if len(v):
    print(min(v))
else:
    print("-1")