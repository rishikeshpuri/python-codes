
def count_character(char):
    dict={}
    for n in char:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(count_character("thequickbrownfoxjumpsoverthelazydog"))
