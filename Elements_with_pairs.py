n=int(input())
x=list(map(int,input().split()))
if n%2==1:
    x.append(0)
    print(*x)
else:
    print(*x)
