#Write a python script to sort a tuple.
list=[]
t=eval(input("Enter a tuple string for sort",))
for i in range(t):
    print(i+1,"Enter numbers")
    data=eval(input())
    list.append(data)
    sort(data)
