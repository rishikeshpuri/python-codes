#To accept one complex number from user and display the greater number between real part and imaginary part.
x=int(input("Enter one real number"))
y=complex(input("Enter one imaginary number"))
if x>y:
    print("%d is greater number"%x)
else:
    print("%d is greatest number"%y)
