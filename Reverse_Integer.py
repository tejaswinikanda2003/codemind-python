
n=int(input())
temp=n
if(n<0):
    n=abs(n)
rev=0
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp<0):
    print(-rev)
else:
    print(rev)