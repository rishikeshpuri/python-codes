x=int(input("Enter lower limit"))
y=int(input("Enter upper limit"))
for num in range(x,y+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                pass
        else:
            print("{} is prime number".format(num))
    else:
        print("not prime number")