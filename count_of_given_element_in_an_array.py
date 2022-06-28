n=int(input())
a=list(map(int,input().split()))
z=int(input())
for i in range(len(a)):
    b=a.count(z)
print(b)