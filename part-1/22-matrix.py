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



# three buildings, 15 floors, 20 rooms

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
