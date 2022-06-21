s=input()
a=0
b=0
for i in range(0,len(s)):
    if(s[i]=='z' or s[i]=='Z'):
        a+=1
    elif(s[i]=='o' or s[i]=='O'):
        b+=1
if(2*a==b):
    print('Yes')
else:
    print('No')
