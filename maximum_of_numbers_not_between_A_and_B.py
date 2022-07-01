def mon(x):
    y=[]
    for i in x:
        if i<n or i>m:
            y.append(i)
    if len(y):
        print(max(y))
    else:
        print("-1")
    
    
    
    
n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
mon(x)