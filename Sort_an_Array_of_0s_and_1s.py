n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if(a[i]==0):
        b.append(a[i])
    elif(a[i]!=0):
        c.append(a[i])
b.extend(c)
print(*b)