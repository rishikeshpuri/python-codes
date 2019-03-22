def str_len(str):
    w_len=[]
    for i in str:
        w_len.append((len(i),i))
    w_len.sort()
    return w_len[-1][1]
print(str_len((["PHP", "Exer", "Bac"])))