for i in range(10):
    print(i)

print(
'''
-
'''
)

for i in range(2, 8):
    print(i)


print('-')


for i in range(2, 18, 3):
    print(i)


print('-')


text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break

    print(letter, end="")
