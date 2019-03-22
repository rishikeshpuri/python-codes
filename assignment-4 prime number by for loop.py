#To check whether a given number is prime or not.
n=int(input("enetr a number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime number",n)
            break
    else:
            print("prime number",n)
else:
    print("not prime number")
