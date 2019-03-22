#To calculate sum of first N natural number. Value of N taken from user.
n=int(input("Enter a number"))
s=0
while n>0:
    s=s+n
    n=n-1
print("Sum of 1st natural number is:",s)
