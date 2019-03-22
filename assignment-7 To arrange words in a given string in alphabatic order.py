#To arrange words in a given string in alphabatic order.
s=input("Enter a string")
words=s.split(' ')
words.sort()

print("Words are arranged in alphabatic order")
for word in words:
    print(word)
