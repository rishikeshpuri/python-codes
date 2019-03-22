num=int(input("Enter a number"))
a=0
b=1
if num<=0:
    print("Not possible")
elif num==1:
    print(a)
elif num>=2:
    print("{},{}".format(a,b),end="")
    for i in range(2,num):
        c=a+b
        print(",{}".format(c),end="")
        a=b
        b=c