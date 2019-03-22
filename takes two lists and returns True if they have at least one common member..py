def common_member(str1,str2):
    result =False
    for x in str1:
        for y in str2:
            if x==y:
                result= True
                return result
print(common_member([1,2,3,4,5], [5,6,7,8,9]))
print(common_member([1,2,3,4,5], [6,7,8,9]))
