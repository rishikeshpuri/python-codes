def strings(str1,str2):
    x=str1[:2]
    y=str2[:2]
    a=x+str2[2:]
    b=y+str1[2:]
    z=a+' '+b
    return z
print(strings('abc', 'xyz'))
    