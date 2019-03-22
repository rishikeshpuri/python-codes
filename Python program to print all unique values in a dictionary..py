'''
lis=[{"abc": "movie"},{"abc": "sports"},{"abc":"music"},{"xyz": "music"},
     {"pqr": "movies"},{"pqr": "sports"}, {"pqr": "news"}, {"pqr": "sports"}]
'''


l=[{'a':1},{'a':2},{'a':3},{'a':1},{'b':1},{'b':1},{'b':2},{'b':2},{'c':1},{'c':2},{'c':3},{'c':1}]

s= set()
for dic in l:
    for val in dic.values():
        s.add(val)
print(s)