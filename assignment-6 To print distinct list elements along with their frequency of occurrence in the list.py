#To print distinct list elements along with their frequency of occurrence in the list.
'''
l=[eval(x) for x in input("Enter list element").split(',')]
element=eval(input("Enter element value"))
count=0
while count<len(l):
    if l[count]==element:
        count=count+1
        break
        print(count)
'''


list=[]
n=int(input("Enter the length of list"))
for i in range(n):
    print("Enter Number")
    data=int(input())
    list.append(data**2)
    list.count()
    
print("square of first N natural number:",list)
    

     
