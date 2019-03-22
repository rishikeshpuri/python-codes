x=int(input("Enter a number"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("{} in not prime number".format(x))
            break
    else:
            print("{} is prime number".format(x))
else:
    print('not prime number')