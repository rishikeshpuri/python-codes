#To check nature of roots of given quadritic equation.
a=float(input("Enter a "))
b=float(input("Enter b"))
c=float(input("Enter c"))
r=b**2-4*a*c
if r>0:
    print("%d Number is real and unequal number"%r)
elif r<0:
    print("%d Number is real number"%r)
else:
    print("%d Number is real and equal number"%r)
    
