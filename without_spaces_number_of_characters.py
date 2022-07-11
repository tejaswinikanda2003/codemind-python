a=input()
b=[]
s=" "
for i  in a:
    if i not in s:
        b.append(i)
print(len(b))