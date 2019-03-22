n=int(input("Enter 1st no"))
m=int(input("Enter 2nd no"))
x=0
z=0
if n>1:
    for i in range(2,n):
        if (n)%i==0:
            x+=i
            break
            
if m>1:
    for y in range(2,m):
        if (m)%y==0:
            z+=y
            break
print("numbers are co prime" if x!=z else "not co prime")
   
#error
