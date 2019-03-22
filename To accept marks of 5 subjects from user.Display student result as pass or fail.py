"""
To accept marks of 5 subjects from user.Display student result as pass or fail.
If the student pass then also display his percentage or division
"""
a=float(input("Enter 1st subject number"))
b=float(input("Enter 2nd subject number"))
c=float(input("Enter 3rd subject number"))
d=float(input("Enter 4th subject number"))
e=float(input("Enter 5th subject number"))
percent=(a+b+c+d+e)/5
if percent>=40:
    print("The student is pass")
    print("%d is the percent"%percent)
    print("1ST Division")
else:
    print("The student is fail")
    print("%d is the percent"%percent)

