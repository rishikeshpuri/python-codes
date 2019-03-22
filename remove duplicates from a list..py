def remove_duplicate(num):
    l=[]
    for n in num:
        if n not in l:
            l.append(n)

    return l
print(remove_duplicate([2, 4, 10, 20, 5, 2, 20, 4]))

'''
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
'''