# creates a matrix

EMPTY = 'B'
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print(board)


# and this is equal to...

board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)
