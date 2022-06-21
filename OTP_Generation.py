n=int(input())
a=[]
s=" "
while(n!=0):
    r=n%10
    if(r%2!=0):
       a.append(r**2)
    n=n//10
k=a[::-1]
str=map(str,k)

m=list(str)
k="".join(m)
print(k)