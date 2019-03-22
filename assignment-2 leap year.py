#To check if a year is leap year or not.
x=int(input("Enter a Year to check it is leap year or not"))
if x%400==0 or x%4==0 and x%100!=0:
    print("%d is a leap year"%x)
else:
    print("%d not a leap year"%x)
