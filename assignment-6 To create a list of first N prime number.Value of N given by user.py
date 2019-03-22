#To create a list of first N prime number.Value of N given by user.
l=[eval(x) for x in input("Enter list element").split(',')]
element=eval(input("Enter element value"))




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
    list.append(num)
print("are the prime number upto",list)



#error
