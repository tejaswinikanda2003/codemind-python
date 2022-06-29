n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=set(x)
b=set(y)
d=[]
for i in a:
    if i not in b:
        d.append(i)
for k in b:
    if k not in a:
        d.append(k)
print(len(d))