#To count occurrence of a given character in a given string.
s=str(input("Enter a string"))
s=s.lower()
alphabet="abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
for char in s:
    if char in alphabet:
        count=s.count(char)
    print(char,':',count)
