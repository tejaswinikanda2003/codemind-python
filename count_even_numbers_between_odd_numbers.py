n=int(input())
x=list(map(int,input().split()))
for i in range(len(x)):
    if x[i]%2==1:
        break
for k in range(len(x)-1,-1,-1):
    if x[k]%2!=0:
        break
c=x[i+1:k]
d=0
for j in c:
    if j%2==0:
        d=d+1
print(d)