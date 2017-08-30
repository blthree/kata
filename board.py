import itertools
# 8x6 board
# columns are letters A thru F
# rows are numbers 1 thru 8
#letters = ['A', 'B', 'C', 'D', 'E', 'F']
#numbers = [1,2,3,4,5,6,7,8]
#keys = [a+str(b) for a in letters for b in range(1, 9)]
#spaces = {k: 0 for k in keys}
#columns = list([l+str(n) for n in numbers] for l in letters)
#rows = list([l+str(n) for l in letters] for n in numbers)
#rows = dict(zip(numbers,list([l+str(n) for l in letters] for n in numbers)))
#columns = dict(zip(letters,list([l+str(n) for n in numbers] for l in letters)))

board="""
......O.
OOO...O.
......O.
........
...OO...
...OO...
"""
i=0
loaded = []
for l in board.split('\n'):
    if len(l) == 8:
        loaded.append(list(l))
        i += 1
#print('\n'.join([''.join([y for y in x])for x in loaded]))
def broadcast(matrix):
    broadcasted = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            broadcasted[j][i] = matrix[i][j]
    return broadcasted
def pretty_print(matrix):
    return '\n'.join([''.join([y for y in x]) for x in matrix])
def get_neighbors(matrix):
    neighbors = itertools.product([1, -1, 0], [1, -1, 0])
    #[(1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0), (0, 1), (0, -1), (0, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(i,j)

            #print(matrix[i+1][j-1])
            #print(a)
            print('\n')


print(pretty_print(loaded))
#print(pretty_print(broadcast(loaded)))
print('')
#print(get_neighbors(loaded))
matrix = loaded.copy()
neighbors = list(itertools.product([1, -1, 0], [1, -1, 0]))
empty = list([[[] for j in range(len(matrix[0]))] for i in range(len(matrix))])
e2 = empty.copy()
for n in neighbors:
    for i in range(0,6):
        for j in range(0,8):
            if n != (0, 0) and (0 <= i + n[0] < len(matrix) and j + n[1] >= 0 and j + n[1] < len(matrix[i])):
                empty[i][j].append(matrix[i+n[0]][j+n[1]])
#print(empty)
print('\n')
i=5
e3 = [[[matrix[i+n[0]][j+n[1]] for n in neighbors if n != (0, 0) and (0 <= i + n[0] < len(matrix) and j + n[1] >= 0 and j + n[1] < len(matrix[i]))].count('O') for j in range(0,8)] for i in range(0, 6)]
#print(e3)
mout = loaded.copy()
for i in range(0, 6):
    for j in range(0, 8):
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



"""
1. Any	live	cell	with	fewer	than two	live	neighbors	dies,	as	if	caused	by	underpopulation.
2. Any	live	cell	with	more	than	three	live	neighbors	dies,	as	if	by	overcrowding.
3. Any	live	cell	with	two	or	three	live	neighbors	lives	on	to	the	next	generation.
4. Any	dead	cell	with	exactly	three	live neighbors	becomes	a	live	cell.
5. A	cell’s	neighbors	are	those	cells	which	are	horizontally,	vertically	or	
diagonally	adjacent.	Most	cells	will	have	eight	neighbors.	Cells	placed	on	the	
edge	of	the	grid	will	have	fewer."""

