nterms = int(input())

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
     print("not fibi")
# if there is only one term, return n1
elif nterms==1:
  print(n1)
# generate fibonacci sequence
else:

   while count < nterms:
       print(n1,end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
