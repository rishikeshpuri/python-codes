def add_str(str):
    z=str[-3:]
    len1=len(str)
    if z=='ing':
        a=str+'ly'
        return a
    elif len1>2:
        b=str+'ing'
        return b
    else:
        return str
print(add_str('abcing'))
print(add_str('abc'))
print(add_str('ab'))