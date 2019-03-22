def appearence(str):
    if 'not' in str:
        x=str.replace('not','')
        return x
    elif 'good' in str:
        y=str.replace('good', 'not good')
        return y
    elif 'poor' in str:
        y = str.replace('poor', 'good')
        return y

print(appearence('The lyrics is not that poor!'))
print(appearence('The lyrics is poor!'))