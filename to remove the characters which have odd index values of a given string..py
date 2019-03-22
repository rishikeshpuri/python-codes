def remove_odd(str):
    result=""
    for i in range(len(str)):
        if i%2==0:
            result=result+str[i]
    return result
print(remove_odd('abcdef'))