def div(i):
    n=i
    c=0
    while(i):
        r=i%10
        if r==0:
            break
        elif n%r==0:
            c=c+1
        i=i//10
    return c    
    
a=int(input())
b=int(input())
for i in range(a,b+1):
   if i<10:
       print(i,end=" ")
   else:
        l=len(str(i))
        p=div(i)
        if l==p:
            print(i,end=" ") 