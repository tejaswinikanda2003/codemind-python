n=int(input())
a=list(map(int,input().split()))
s=p=0
for i in range(n):
    if i%2==0:
        s+=a[i]
    else:
        p+=a[i]
res=abs(s-p)
print(res)