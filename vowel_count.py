a=input()
v="aeiouAEIOU"
c=0
for i in a:
    if i in v:
        c+=1
print(c)