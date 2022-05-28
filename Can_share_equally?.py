x,y=map(int,input().split())
t=x*1+y*2
if x==0 and y%2==0:
    print('YES')
elif x==0 and y%2!=0:
    print('NO')
elif t%2==0:
    print('YES')
else:
    print('NO')