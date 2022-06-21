n=int(input())
c=0
f=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]%2==0):
        c=c+1
    else:
        f=f+1
print(c,f)