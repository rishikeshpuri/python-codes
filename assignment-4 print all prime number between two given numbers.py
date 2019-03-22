#To print all prime number between two given numbers.
lower=int(input("enter lower number"))
upper=int(input("enter upper number"))
for e in range(lower,upper+1):
    if e>1:
        for i in range(2,e):
            if e%i==0:
                break
        else:
            print("prime number are",e)
            
    
