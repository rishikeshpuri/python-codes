#To accept one complex number from user and display the greater between real and imaginary part.
c=complex(input("Enter a complex number"))
if c.real>c.imag:
    print("%d is greater"%(c.real))
elif c.real<c.imag:
    print("%d is greater"%(c.imag))
else:
    print("both are same")
