#To calculate sum of all the integers of the list given by user.
list=[]
n=int(input("Enter the length of list"))
x=0
for i in range(n):
    print("Enter Number")
    data=int(input())
    list.append(data)
print("sum of all the integers is:",sum(list))
