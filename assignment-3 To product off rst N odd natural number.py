#To calculate product of first N odd natural number.Value is taken from user.
n=int(input("enter a number"))
i=1
sum=1
while i<=n:
    if i%2!=0:
        sum=sum*i
    i=i+1
print(sum)
      
