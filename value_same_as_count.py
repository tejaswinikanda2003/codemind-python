n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    if i not in y:
        y.append(i)
c=0
for k in y:
    if x.count(k)==k:
        c=c+1
print(c)