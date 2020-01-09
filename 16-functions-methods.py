ns = [0, 1, 3, 4, 5]

ns.append(6)
ns.insert(2, 2)

print(ns)


myList = []  # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)


myList = []  # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)


aux = 0
arr = []

while aux != -1:
    aux = int(input('Número: '))

    if aux != -1:
        arr.append(aux)

print(arr)