def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    return False
def fac(n):
    x=[]
    for k in range(2,n):
        if n%k==0:
            if pn(k):
                 print(k,end=" ")
n=int(input())
if pn(n)==False:
    fac(n)
else:
    print("-1")