#print all prime numbers for a given number.
n=int(input("enter a number"))
for n in range(0,n+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
print("are the prime number upto",n)
