n=int(input())
for i in range(n):
    a=str(input())
    r=a[::-1]
    if(a==r):
        print("True")
    else:
        print("False")