#To check if a year is leap year or not.
x=int(input("Enter a Year to check it is leap year or not"))
if x%400==0:
    print("%d year is leap year"%x)
elif x%100==0:
    print("%d year is not leap year"%x)
elif x%4==0:
    print("%d year is leap year"%x)
