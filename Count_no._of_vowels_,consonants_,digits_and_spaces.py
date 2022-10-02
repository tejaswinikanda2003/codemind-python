n=input()
c=['a','e','i','o','u']
v=[]
t=[]
d=[]
s=[]
for i in n:
    if i in c:
        v.append(i)
   
    if i.isdigit():
        d.append(i)
    if i.isspace():
        s.append(i)
    if i not in c and i not in d and i not in s:
        t.append(i)
print("Vowels:",len(v))
print("Consonants:",len(t))
print("Digits:",len(d))
print("White spaces:",len(s))
        