def bin(x):
    d=len(x)
    c=0
    for i in x:
        if i==0 or i ==1:
            c=c+1
    if c==d:
        print("True")
    else:
        print("False")
    
n=int(input())
x=list(map(int,input().split()))
bin(x)