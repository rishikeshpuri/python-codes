#To check nature of roots of given quadritic equation and solve itONLY FOR REAL NUMBER.
import math
a=float(input("Enter a "))
b=float(input("Enter b"))
c=float(input("Enter c"))
r=b**2-4*a*c
w=(-b-math.sqrt(r))/(2*a)
q=(-b-math.sqrt(r))/(2*a)
print("The solution is,w={0}q={1}".format(w,q))
