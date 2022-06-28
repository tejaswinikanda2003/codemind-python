n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    sum=sum+a[i]
avg=(sum)//n
if avg  in a:
    print("True")
else:
    print("False")