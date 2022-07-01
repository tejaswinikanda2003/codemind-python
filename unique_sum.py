x=int(input())
z=list(map(int,input().split()))
y=set(z)
s=0
for i in y:
    s=s+i
print(s)