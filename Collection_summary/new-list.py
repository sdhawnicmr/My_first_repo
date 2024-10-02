#Collection = a single variable tha stores multiple values

fruits = ["apple", "cherry", "banana","watermelon"]
print(fruits)  # ["apple", "cherry", "banana","watermelon"]
#To acces the elemnets inside list, we use "index" i.g[i]
print(fruits[1])  #cherry
#print(fruits[1:])
#to find the index numbers of an element, use "find"
print(fruits.index("cherry"))  #1
# To find length of an element
print(len(fruits))

for fruit in fruits:
    print(fruit)

print(dir(fruits))
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort']

# To add one element at the end of a list
fruits.append("Guava")
print(fruits)

# To add list of elements at the end of first list
fruits.extend(["lemon","Orange","Mango"])
print(fruits)

# to add an element at any particular index
fruits[0] = "pineapple"
print(fruits)

# to remove an element
fruits.remove("pineapple")
print(fruits)

# Insert method to add an element at a particlar index
fruits.insert(0,"apple")
print(fruits)

#To sort the elements in a list
fruits.sort()
print(fruits)

# To Reverse the elements in a list
fruits.reverse()
print(fruits)

# To clear list
#fruits.clear()
#print(fruits)

# to count a particular element in a list
print(fruits.count("apple"))


