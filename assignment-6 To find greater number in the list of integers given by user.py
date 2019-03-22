#To find greater number in the list of integers given by user.
list=[]
n=int(input("Enter the length of list"))
for i in range(1,n+1):
    print("Enter Number")
    data=int(input())
    list.append(data)
    list.sort()
print("Greatest number is:",list[n-1])
