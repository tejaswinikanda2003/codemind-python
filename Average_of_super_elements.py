n=int(input())
x=list(map(int,input().split()))
s=0
c=0
y=[]
for k in x:
    if k not in y:
        y.append(k)
for i in y:
    if x.count(i)==i:
        s=s+i
        c=c+1
if c!=0:
    avg=s/c
    print(format(avg, '.2f'))
else:
    print("-1")