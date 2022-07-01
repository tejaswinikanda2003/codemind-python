n=int(input())
x=list(map(int,input().split()))
z=[]
for i in x:
    if i%2==0:
        c=x.index(i)
        break
for k in range(len(x)-1,-1,-1):
    if x[k]%2==0:
        d=k
        break
y=x[c+1:d]
f=0
for j in y:
    if j%2==1:
        f=f+1
print(f)
       