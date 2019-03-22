def count_word(str):
    count=dict()
    words=str.split()
    for n in words:
        if n in count:
            count[n]=count[n]+1
        else:
            count[n]=1
    return count
print(count_word('the the the the quick brown fox jumps over the lazy dog'))