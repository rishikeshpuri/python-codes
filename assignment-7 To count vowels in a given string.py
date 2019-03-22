#To count vowels in a given string.
s=input("Enter the string")
vowels=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels+=1
print("number of vowels are",vowels)
