#To check whether a given string is palindrome or not BY SLICING OPERATION.
s=input("Enter a string")
if s==s[::-1]:
    print("palindrome")
else:
    print("Not palindrome")
