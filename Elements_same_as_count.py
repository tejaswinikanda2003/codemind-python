n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    if i not in y:
        y.append(i)
v=[]
for i in y:
    z=x.count(i) 
    if z==i:
        v.append(i)
if len(v)==0:
    print(-1)
else:
    print(*v)