n=int(input())
x=list(map(int,input().split()))
s=0
for i in range(len(x)):
    if x[i]%2==1:
        break
    else:
        s=s+x[i]
print(s)
        
  