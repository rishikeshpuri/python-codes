#LCM/LCD of 2 numbers.
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
if x>y:
    min1=x
else:
    min1=y
while True:
    if(min1%x==0 and min1%y==0):
        print("LCM is:",min1)
        break
    min1=min1+1




#clear nhi hua hai.
