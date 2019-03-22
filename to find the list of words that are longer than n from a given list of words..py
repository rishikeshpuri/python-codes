def long_word(str,n):
    word_len=[]
    s=str.split(" ")
    for x in s:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_word("The quick brown fox jumps over the lazy dog",3))
