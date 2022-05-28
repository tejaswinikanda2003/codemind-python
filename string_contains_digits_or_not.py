n=int(input())
while n!=0:
    t=input()
    for i in t:
        if i in '123456789':
            print("Yes")
            break
    else:
        print("No")
    n=n-1