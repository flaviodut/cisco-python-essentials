# The 'problem' is that list1 and 2 points to the same memory location
# When you store a list in a variable, the var name store the memory location and not the list itself
list1 = [1]
list2 = list1
list1[0] = 2
print(list1, list2)

# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list1, list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

# You can omit the 'start'
myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

# or the 'end'
myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

# Delete part of the list
myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

# Delete the content of the list stored on memory, not the variable
myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

# Delete the variable
myList = [10, 8, 6, 4, 2]
del myList
print(myList)  # this will return a exception error

# Check if value is stored in the list
myList = [0, 3, 12, 8, 2]
print(5 in myList)
print(5 not in myList)
print(12 in myList)