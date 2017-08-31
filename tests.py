import unittest

class my_tests(unittest.TestCase):
    import board
    def setUp(self):
        self.test_board = ['......O.','OOO...O.','......O.','........','...OO...','...OO...']
        self.output_board =
        self.sample_board = 'sample_board'
    def test_file_read(self):
        import board
        self.assertEqual(board.read_board_file(self.sample_board), self.test_board)
    def test_output(self):
        import board
        self.assertEqual(board.read_board_file(self.sample_board))
        pass


if __name__ == '__main__':
    import board
    my_tests()
