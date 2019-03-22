'''
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sum(d.keys()))
print(sum(d.values()))
'''

def sum_dic(dic):
    multi= 1
    for i in dic:
        multi*=dic[i]
    return multi
d= {1: 10, 2: 20, 3: 30}
print(sum_dic(d))