# Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input('enter number'))

dic={}

for i in range(1 , n+1):
    dic[i]=i*i

print(dic)