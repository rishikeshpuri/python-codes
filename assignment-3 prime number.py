#To check whether a given number is prime or not.
n=int(input("Enter a number"))
i=2
x=0
while i<n:
    if n%i==0:
        x=1
        print("not prime number")
        break
    i=i+1
if x==0:    
    print("prime number")




        
