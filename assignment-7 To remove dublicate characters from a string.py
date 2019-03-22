#To remove duplicate characters from a string.
names=[]
n=int(input("Enter how many names you want to enter"))
for i in range(n):
    print(i+1,"Enter the name")
    names.append(input())
s=set(names)
names=list(s)
for x in names:
    print(x)
