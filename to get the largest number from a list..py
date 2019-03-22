'''
a=[]
n=int(input("Enter number of elements"))
for i in range(n):
    b=int(input('enter element'))
    a.append(b)
a.sort()
print("largest number",a[-1])
'''

def max_num(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max
print(max_num([1,2,3]))