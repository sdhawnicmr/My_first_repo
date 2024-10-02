fruits = {"apple", "cherry", "banana","watermelon"}
print(fruits) #Unordered

print(dir(fruits))
#'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

fruits.add("coconut")
print(fruits)

fruits.remove("watermelon")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)
