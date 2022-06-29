n = int(input())
m = list(map(int,input().split()))
a = int(input())
l = m.index(a)
k = m[:l+1]
print(sum(k))
        