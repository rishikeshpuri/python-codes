def count_string(str):

    num=0
    for i in str:
        if len(i)>1 and i[0]==i[-1]:
            num=num+1
    return num
print(count_string(['abca','xyz','aba','121']))
        