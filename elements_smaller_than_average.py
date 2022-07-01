n=int(input())
x=list(map(int,input().split()))
c=[]
s=sum(x)
l=len(x)
a=s//l
for i in x:
    if i<=a:
        c.append(i)
print(len(c))
