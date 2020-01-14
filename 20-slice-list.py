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
