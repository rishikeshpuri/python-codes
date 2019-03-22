'''
s=input("enter string")
l=len(s)
print(l)
'''
def string(s):
    count=0
    for i in s:
        count=count+1
    return count
print(string('asdf'))