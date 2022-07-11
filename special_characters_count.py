a=input()
s=[]
for i in a:
    if i.isalpha():
        s.append(i)
    if i in ' ':
        s.append(i)
print(len(a)-len(s))