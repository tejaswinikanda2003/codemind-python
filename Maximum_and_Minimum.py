n=int(input())
x=list(map(int,input().split()))
y=[]
v=[]
for i in x:
    if i not in y:
        y.append(i)
for k in y:
    if x.count(k)==k:
        v.append(k)
if len(v):
    print(v[0],v[-1])
else:
    print("-1")