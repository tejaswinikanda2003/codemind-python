def fact(k):
    p=1
    for i in range(1,k+1):
        p=p*i
    return p
n=int(input())
q=n
s=0
while q:
    r=q%10
    s=s+fact(r)
    q=q//10
if s==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")