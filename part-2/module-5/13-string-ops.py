# concatenate
print('Aaa' + 'Bbb')

# multiplicate
print('Aaa' * 4)

# unicode code point value with ord()
print(ord('a'))

arr = []

str = 'Flávio'
for letter in str:
    print(ord(letter))
    arr.append(ord(letter))

# ord reverse is chr()
for n in arr:
    print(chr(n))
