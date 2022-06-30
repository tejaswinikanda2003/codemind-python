import math
def nod(a):
    c=0
    while a>0:
        r=a%10
        c+=1
        a//=10
    return c
a,b=map(int,input().split())
fb=lb=diff=0
lb=a%math.pow(10,b)
fb=a//math.pow(10,nod(a)-b)
diff=fb-lb
if diff<0:
    diff*=-1
print("{:.0f}".format(diff))
