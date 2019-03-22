#To calculate average of tuple value.Assuming values are of int type only.
list=[]
x=eval(input("Enter how many values for average "))
sum=0
for i in range(x):
    print(i+1,"enter value")
    data=eval(input())
    list.append(data)
    sum=sum+data
avg=sum/x
   
    

    
print("Average is",avg,type(x))
