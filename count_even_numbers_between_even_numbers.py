n = int(input())
m = list(map(int,input().split()))
z = 0
for i in m:
    if i%2 == 0:
        c= m.index(i)
        break
for j in range(len(m)-1,-1,-1):
    if m[j]%2 == 0:
        d = j
        break
x = m[c+1:d]
for i in x:
    if i % 2 ==0:
        z = z+1
print(z)