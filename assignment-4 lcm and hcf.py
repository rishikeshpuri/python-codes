#LCM and HCF.
x=int(input("Enter 1st number")) 
y=int(input("Enter 2nd number")) 
a=x  
b=y 
while(b!=0):
    t=b 
    b=a%b 
    a=t 
hcf=a
lcm=(x*y)/hcf
print("HCF of %d and %d is %d\n"%(x,y,hcf))
print("LCM of %d and %d is %d\n"%(x,y,lcm))
'''
b = 8 = 2 * 2 * 2
a = 36 = 2 * 2 * 3 * 3
 
a % b = 4
b =  






'''

