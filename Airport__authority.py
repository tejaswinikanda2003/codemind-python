n=int(input())
c=0
a=[]
for i in range(0,n):
    k=int(input())
    a.append(k)
    
t=int(input())
for i in range(0,len(a)):
    if(a[i]<=t):
        c=c+1
    elif(a[i]>t):
        c=c+2
print(c)