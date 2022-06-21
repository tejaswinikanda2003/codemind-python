t=int(input())
for i in range(0,t):
    n=input()
    k=len(n)
   # print(k)
    f=0
    v="0123456789"
    for i in n:
        if(i in v):
            f=f+1
    #print(f)
    if(f==k):
        print(True)
    else:
        print(False)