#To count word in a given string.
s=input("Enter a string")
word=input("Enter word")
a=[]
count=0
a=s.split(' ')
for i in range(0,len(a)):
    if word==a[i]:
        count=count+1
print("count of the word is",count)
