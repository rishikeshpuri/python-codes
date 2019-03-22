d={'a':1,'b':2,'c':3,"d":4,'e':5}
print('key  value   count')
for count,(key,value) in enumerate(d.items(),1):
    print(key,'    ',value,'    ',count)