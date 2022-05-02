num = int(input())
sqr = num*num #square of num
sumOfDigit = 0

#calculating sum of digits of sqr
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10

if (num == sumOfDigit):
    print("Neon Number")
else:
    print("Not Neon Number")