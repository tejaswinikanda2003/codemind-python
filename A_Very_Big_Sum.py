n=int(input())
total = 0
a=list(map(int,input().split()))
for i in range(0, len(a)):
    total = total + a[i]
print( total)
