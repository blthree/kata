def broadcast(matrix):
    broadcasted = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            broadcasted[j][i] = matrix[i][j]
    return broadcasted

def get_neighbors(matrix):
    neighbors = itertools.product([1, -1, 0], [1, -1, 0])
    #[(1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0), (0, 1), (0, -1), (0, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(i,j)

            #print(matrix[i+1][j-1])
            #print(a)
            print('\n')

# get neighbors using nested for loops
# replaced by generator
for n in neighbors:
    for i in range(0,6):
        for j in range(0,8):
            if n != (0, 0) and (0 <= i + n[0] < len(matrix) and j + n[1] >= 0 and j + n[1] < len(matrix[i])):
                empty[i][j].append(matrix[i+n[0]][j+n[1]])

# old game logic in nested for loops
# replace by generator
mout = matrix.copy()
for i in board_height:
    for j in board_width:
        if matrix[i][j] == 'O':
            if e3[i][j] < 2 or e3[i][j] >3:
                mout[i][j] = '.'
            else:
                mout[i][j] = 'O'
        elif matrix[i][j] == '.':
            if e3[i][j] == 3:
                mout[i][j] = 'O'
            else:
                e3[i][j] = '.'
        else:
            raise ValueError("Cell value must be '.' or 'O'")
print(pretty_print(mout))