lower=int(input("Enter lower limit"))
upper=int(input("Enter upper limit"))
for num in range(lower,upper+1):
    sum=0
    l = len(str(num))
    i=num

    while i>0:
        digit=i%10
        sum=sum+digit**l
        i//=10
    if num==sum:
        print(num)
        