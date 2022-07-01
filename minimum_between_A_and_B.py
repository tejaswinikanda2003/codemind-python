vn=int(input())
x=list(map(int,input().split()))
n,m=list(map(int,input().split()))
#print(x)
#print(n,m)
v=[]
for i in x:
    if i>=n and i<m:
        v.append(i)
#print(v)
if len(v):
    print(min(v))
else:
    print("-1")
