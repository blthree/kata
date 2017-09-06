#!/usr/bin/env python


import argparse
import logging
from board import run_life, str_to_matrix, matrix_to_str, read_board_file


# Run simulation
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("Running simulation for {0} cycle(s) using file: '{1}' as starting board"
                 .format(args.cycles, args.board_file))

    board = str_to_matrix(read_board_file(args.board_file))
    output = run_life(board, int(args.cycles))
    print("Initial Board State: {0}".format(matrix_to_str(output[0])))
    print("Final Board State: {0}".format(matrix_to_str(output[-1])))


# define and parse CLI arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Conway's Game of Life Simulator")
    # TODO Specify your real parameters here.
    parser.add_argument(
        "board_file",
        help="File containing game board",
        metavar="BOARD_FILE")
    parser.add_argument(
        "-v",
        "--verbose",
        help="displays intermediate board states as well as starting and final state",
        action="store_true")
    parser.add_argument(
        "-c",
        "--cycles",
        help="# of simulation cycles, defaults to 1 if omitted")
    args = parser.parse_args()
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    # run simulation for 1 cycle if unless otherwise specified
    if not args.cycles:
        args.cycles = 1

    main(args, loglevel)
