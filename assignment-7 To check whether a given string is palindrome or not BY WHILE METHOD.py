#To check whether a given string is palindrome or not BY WHILE METHOD.
s=int(input(("Enter a number")))
temp=s
rev=0
while s>0:
    d=s%10
    rev=rev*10+d
    s=s//10
if rev==temp:
    print("palindrome",)
else:
    print("not palindrome")
