WHITE_PAWN = 'W'

row = []

for i in range(8):
    row.append(WHITE_PAWN)

print(row)

# this is equal to...
row = [WHITE_PAWN for i in range(8)]

print(row)


# another examples

squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]
odds = [x for x in squares if x % 2 != 0]

print(squares)
print(twos)
print(odds)
