n = int(input())
m = list(map(int,input().split()))
sum1 = 0
for i in range(len(m)):
    if m[i]%2 == 0:
        break
    else:
        sum1 += m[i]
print(sum1)   