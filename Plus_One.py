a=int(input())
arr=list(map(int,input().split()))
num=0
for i in arr:
    num=(num*10)+i
num+=1
arr2=[]
while num>0:
    rem=num%10
    arr2.append(rem)
    num//=10
arr2.reverse()
for i in arr2:
    print(i,end=" ")