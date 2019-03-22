#To print index of all occurrence of a given element in a given list.
l=[eval(x) for x in input("Enter list element").split(',')]
element=eval(input("Enter element value"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
    index+=1
