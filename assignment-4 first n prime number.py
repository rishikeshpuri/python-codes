#To print first n prime number. Value of n is given by user.
number=int(input("Enter a number"))
for num in range(0,number+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                pass
        else:
            print(num)
    else:
        pass
print("are the prime number upto",number)
