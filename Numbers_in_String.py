a=input()
val=0
for i in a:
    if i.isdigit():
        val+=ord(i)-48
print(val)