#To print all Armstrong numbers under 1000.

for i in range(0,1000+1):
    num=i
    sum=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        sum=sum+digit**n
        i=i//10
    if num==sum:
        print(num)
