#To create a list of square of first N natural number.
list=[]
n=int(input("Enter the length of list"))
for i in range(n):
    print("Enter Number")
    data=int(input())
    list.append(data**2)
    list.sort()
    
print("square of first N natural number:",list)
    
