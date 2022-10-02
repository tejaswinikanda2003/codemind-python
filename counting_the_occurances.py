n=input()
p=input()
c=0

for i in n:
    if i==p:
        c+=1
if p not in n:
    print(-1)
else:
    print(c)