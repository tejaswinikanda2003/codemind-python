a=int(input())
l=map(int,input().split())
b=int(input())
c=0
for i in range(a):
    if b in l:
        c=c+1
print(c)