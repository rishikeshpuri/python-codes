def specified_list(str):
    x=str[0]
    y=str[4]
    z=str[5]
    a=str.remove(x)
    b=str.remove(y)
    c = str.remove(z)
    return str

print(specified_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))