import itertools
from functools import reduce
def pretty_print(matrix):
    return '\n'.join([''.join([y for y in x]) for x in matrix]) +'\n'

def check_len(x,y):
    if len(x) == len(y):
        return y
    else:
        raise ValueError("""Length of line: '{0}' does not match length of previous line '{1}'""".format(y,x))

def game_logic(in_cell, neighbor_count):
    # rules 1, 2, 3
    if in_cell == 'O':
        if neighbor_count < 2 or neighbor_count > 3:
            return '.'
        else:
            return 'O'
    # rule 4
    elif in_cell == '.':
        if neighbor_count == 3:
            return 'O'
        else:
            return '.'
    # raise error if invalid character made it into the game board
    else:
        raise ValueError("Cell value must be '.' or 'O'")

def read_board_file(filename):
    with open(filename) as f:
        return f.read()

board_str = """......O.
OOO...O.
......O.
........
...OO...
...OO..."""

def run_life(board_str, num_iter):
    def compute_next_board(start_state):
        # create matrix containing number of live neighbors for each cell
        live_neighbor_matrix = [[[start_state[y + n[0]][x + n[1]] for n in neighbors if n != (0, 0) and (0 <= y + n[0] < len(start_state) and x + n[1] >= 0 and x + n[1] < len(start_state[y]))].count('O') for x in board_width] for y in board_height]
        # compute next board state
        end_state = [[game_logic(start_state[y][x], live_neighbor_matrix[y][x]) for x in board_width] for y in board_height]
        return end_state

    # validate game board input and store dimensions
    board_list = board_str.split('\n')
    board_width = range(len(reduce(check_len, board_list))) # 8
    board_height = range(len(board_list)) # 6
    matrix = list([list(l) for l in board_list])
    print(pretty_print(matrix))


    print('')
    # generate offsets of possible nieghbors
    neighbors = list(itertools.product([1, -1, 0], [1, -1, 0]))
    # create empty game board
    empty = list([[[] for j in board_width] for i in board_height])
    result = matrix.copy()
    for i in range(num_iter):
        result = compute_next_board(result)
    print(pretty_print(result))

run_life(board_str,3)





rules = """
1. Any	live	cell	with	fewer	than two	live	neighbors	dies,	as	if	caused	by	underpopulation.
2. Any	live	cell	with	more	than	three	live	neighbors	dies,	as	if	by	overcrowding.
3. Any	live	cell	with	two	or	three	live	neighbors	lives	on	to	the	next	generation.
4. Any	dead	cell	with	exactly	three	live neighbors	becomes	a	live	cell.
5. A	cell’s	neighbors	are	those	cells	which	are	horizontally,	vertically	or	
diagonally	adjacent.	Most	cells	will	have	eight	neighbors.	Cells	placed	on	the	
edge	of	the	grid	will	have	fewer."""

