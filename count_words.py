a=input()
arr=list(a.split())
vow=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in arr:
    l=len(i)
    if i[0] in vow and [l-1] not in vow:
        c+=1
print(c)