a=int(input())
l=map(int,input().split())
z=int(input())
for i in range(a):
    if z in l:
        print(True)
        break
else:
    print(False)