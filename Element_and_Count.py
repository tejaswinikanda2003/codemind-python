n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    if i not in y:
        y.append(i)
z=[]
for k in y:
    a=x.count(k)
    print(k, a,end=" ")
#print(z)