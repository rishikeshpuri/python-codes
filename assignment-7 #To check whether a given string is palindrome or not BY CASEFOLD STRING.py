#To check whether a given string is palindrome or not BY CASEFOLD STRING().
s=input("Enter a string")
s=s.casefold()
rev=reversed(s)
if list(s)==list(rev):
    print("palindrome")
else:
    print("not palindrome")
