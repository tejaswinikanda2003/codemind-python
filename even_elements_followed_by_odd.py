n=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
for i in m:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
for k in b:
    a.append(k)
print(*a)