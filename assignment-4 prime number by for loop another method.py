#To check whether a given number is prime or not by another method.
n=int(input("Enter a number"))
factor=0
for i in range(1,n+1):
    if n%i==0:
        factor=factor+1
        
if factor==2:
    print(n,"number is prime")
else:
     print(n,"number is not prime")
