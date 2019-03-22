x=int(input("Enter a number"))
fact=1
if x<1:
    print("{} is not exist".format(x))
elif x==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, x + 1):
        fact = fact * i
    print(fact)
