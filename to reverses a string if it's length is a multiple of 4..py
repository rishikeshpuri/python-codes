def rev_string(str):
    if len(str)%4==0:
        return '' .join(reversed(str))
    return str
print(rev_string('abcd'))
print(rev_string('abcdef'))