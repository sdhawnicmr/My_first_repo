list1= [1,2,3,4,5,6,7,8]
list2 = [10,20,30,40,50,60,70,]

result = dict(zip(list1,list2))
print(result)

for i in result.items():
    print(i)