#To print next prime number of a given number.
n=int(input("Enter a number"))
x=n+1
while True:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print("Next prime number is",x)
        break
    x=x+1
