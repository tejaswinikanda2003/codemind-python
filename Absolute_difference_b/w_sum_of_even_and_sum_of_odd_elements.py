n=int(input())
l=list(map(int,input().split()))
s=p=0
for i in range(n):
    if l[i]%2==0:
        s+=l[i]
    else:
        p+=l[i]
res=abs(s-p)
print(res)