def count_range_in_list(l,min,max):
    count_range=0
    for x in l:
        if min<=x<=max:
            count_range=count_range+1
    return count_range
list1= [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1,40,100))


list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))