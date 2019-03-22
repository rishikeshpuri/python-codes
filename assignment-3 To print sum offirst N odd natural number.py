#To calculate sum of first N odd natural number. Value of N taken from user.
n=int(input("Enter a number"))
x=1
sum=0
while x<=n:
    if x%2==1:
        sum=sum+x
    x=x+1
print(sum)    




    

