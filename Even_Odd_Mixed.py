n=int(input())
q=n
c=0
e=0
o=0
while(q):
    r=q%10
    c=c+1
    if r%2==0:
        e=e+1
    else:
        o=o+1
    q=q//10
if e==c:
    print("Even")
elif o==c:
    print("Odd")
else:
    print("Mixed")