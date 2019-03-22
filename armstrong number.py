n=int(input("Enter a number"))
for i in range(n):
    l=len(str(n))
    sum=0
    i=n
    while i>0:
        digit=i%10
        sum=sum+digit**l
        i=i//10
if n==sum:
    print("{} is armstrong number".format(n))
else:
    print("{} is NOT armstrong number".format(n))