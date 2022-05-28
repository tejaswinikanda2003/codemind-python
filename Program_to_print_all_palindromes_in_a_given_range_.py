def ispalan(k):
    q=k
    s=0
    while(q):
        r=q%10
        s=s*10+r
        q=q//10
    if(s==k):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if ispalan(i):
        print(i,end=' ')