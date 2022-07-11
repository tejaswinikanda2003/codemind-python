a=int(input())
b=list(map(int,input().split()))
m=b
b=set(b)

b=list(b)
v=sorted(b)
if v==m:
    print("yes")
else:
    print("no")
