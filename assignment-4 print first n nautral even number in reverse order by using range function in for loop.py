#print first n nautral even number in reverse order by using range function in for loop.
n=int(input("Enter a number"))
for i in range(n,0,-1):
    if i%2==0:
        print(i)
