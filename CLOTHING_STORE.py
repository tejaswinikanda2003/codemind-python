n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    if(arr[i]==0):
        continue
    else:
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                c+=1
                arr[j]=0
                break
print(c)