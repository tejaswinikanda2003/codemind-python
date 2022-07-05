n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    if i not in y:
        y.append(i)
s=0
for k in y:
    if k%2==1:
        s=s+k
print(s)