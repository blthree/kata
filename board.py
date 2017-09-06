import itertools
from functools import reduce
import logging


def matrix_to_str(matrix):
    return '\n' + '\n'.join([''.join([y for y in x]) for x in matrix]) + '\n'


def check_len(x, y):
    if len(x) == len(y):
        return y
    else:
        raise ValueError("""Length of line: '{0}' does not match length of previous line '{1}'""".format(y, x))


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
        raw_board = f.read()
    return raw_board


def str_to_matrix(board_str):
    # validate game board input and store dimensions
    board_list = board_str.split('\n')
    matrix = list([list(l) for l in board_list if len(l)])
    # print(matrix_to_str(matrix))
    return matrix


board_str = """......O.
OOO...O.
......O.
........
...OO...
...OO..."""


def run_life(matrix, num_iter):
    def compute_next_board(start_state):
        # create matrix containing number of live neighbors for each cell
        live_neighbor_matrix = [[[start_state[y + n[0]][x + n[1]] for n in neighbors
                                  if n != (0, 0)
                                  and (0 <= y + n[0] < len(start_state)
                                       and 0 <= x + n[1] < len(start_state[y]))].count('O')
                                 for x in board_width]
                                for y in board_height]
        # compute next board state
        end_state = [[game_logic(start_state[y][x], live_neighbor_matrix[y][x])
                      for x in board_width] for y in board_height]
        return end_state

    # store dimensions of board
    board_width = range(len(reduce(check_len, matrix)))
    board_height = range(len(matrix))

    # generate offsets of possible neighbors
    neighbors = list(itertools.product([1, -1, 0], [1, -1, 0]))

    result = [matrix.copy()]
    for i in range(num_iter):
        # run game and append to list of each board state
        # this list isn't currently necessary,
        # but simplifies adding features that use intermediate states
        # TODO: add CLI option to disable "caching" intermediate states
        # might cause issues with large boards and many cycles
        result.append(compute_next_board(result[-1]))
        logging.debug("Board state cycle {0}: {1}".format(i + 1, matrix_to_str(result[-1])))
    return result
