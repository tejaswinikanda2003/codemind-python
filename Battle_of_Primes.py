def isprime(k):
    if k==1:
        return False
    else:
        for j in range(2,k//2+1):
            if k%j==0:
                return False
        else:
            return True
a=int(input())
b=int(input())
c=a+b
d=c
while(True):
    c=c+1
    if isprime(c):
        e=c
        break
print(e-d)