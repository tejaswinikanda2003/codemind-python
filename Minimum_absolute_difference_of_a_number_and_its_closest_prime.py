n=int(input())
a=n+1
b=n-1
def pn(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def op(n):
    a=n+1
    b=n-1
    if pn(n):
        print(0)
        return 0
    while pn(a)==False:
        a=a+1
    while pn(b)==   False:
        b=b-1
    y=abs(a-n)
    x=abs(b-n)
    z=y
    s=y
    p=x
    q=x
    if x>y:
        while pn(z)==False:
            z=z+1
        while pn(s)==False:
            s=s-1
        if abs(s-y)>abs(z-y):
            print(z)
        else:
            print(s)
    else:
        while pn(p)==False:
            p=p+1
        while pn(q)==False:
            q=q-1
        if abs(p-x)>abs(q-x):
            print(q)
        else:
            print(p)
op(n)