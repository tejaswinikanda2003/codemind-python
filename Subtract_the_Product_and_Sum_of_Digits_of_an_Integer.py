a=int(input())
su=0
pro=1
while a>0:
    r=a%10
    su+=r
    pro*=r
    a//=10
print(pro-su)