def min_num(list):
    min=list[0]
    for a in list:
        if a<min:
            min=a
    return min
print(min_num([1,2,3]))