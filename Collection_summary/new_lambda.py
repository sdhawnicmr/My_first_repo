import random

#creating list of Random numberes
numbers = [random.randint(1,100) for i in range(10)]
print(numbers)

#Find even or odd
def even(x):
    return x%2==0
evens= list(filter(even,numbers))
print(evens)

#Using Lambda function : used mostly with map, filter, sorted
even_num = list(filter(lambda x:x%2==0, numbers))
print(even_num)
