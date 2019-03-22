#To find greatest among three number.
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
if x>y>z:
    print("%d is greatest number"%x)
if x>z>y:
    print("%d is greatest number"%x)
elif y>x>z:
    print("%d is greatest number"%y)
elif y>z>x:
    print("%d is greatest number"%y)   
elif z>y>x:
    print("%d is greatest number"%z)
elif z>x>y:
    print("%d is greatest number"%z)
