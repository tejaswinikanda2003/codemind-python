n=int(input())
x=list(map(int,input().split()))
a=int(input())
y=[]
n = []
for i in x:
    if i not in y:
        y.append(i)
for k in y:
    z=x.count(k)
    if a==z:
        n.append(k)
if len(n)==0:
    print(-1)
else:
    print(*n)
