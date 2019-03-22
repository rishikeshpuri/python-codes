#To sort a list given by user.
list=[]
n=int(input("Enter length of list"))
for i in range(n):
    print("Enter Number")
    data=int(input())
    list.append(data)
    list.sort()
print(list)
