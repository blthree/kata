import unittest


class ConwayTests(unittest.TestCase):
    def setUp(self):
        self.test_board = ['......O.', 'OOO...O.', '......O.', '........', '...OO...', '...OO...']
        self.matrix_board = [[x for x in row] for row in self.test_board]
        self.input_board_str = '\n'.join(self.test_board) + '\n'
        self.sample_board = 'sample_board.txt'
        self.neighbor_matrix = [[1], [3], [1], [1], [0], [1], [1], [1]]
        self.output_board = ['.O......', '.O...OOO', '.O......', '........', '...OO...', '...OO...']
        self.output_matrix = [[x for x in row] for row in self.output_board]

    def test_file_input(self):
        import board
        self.assertEqual(board.read_board_file(self.sample_board), self.input_board_str)

    def test_str_to_matrix(self):
        import board
        str_board = board.read_board_file(self.sample_board)
        matrix_board = board.str_to_matrix(str_board)
        self.assertEqual(matrix_board, self.matrix_board)

    def test_output(self):
        import board
        self.assertEqual(board.run_life(self.matrix_board, 1)[-1], self.output_matrix)


if __name__ == '__main__':
    import board
    ConwayTests()
