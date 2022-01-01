import pytest
from ex12_utils import *

board_1 = [['T', 'H', 'E', 'T'],
           ['O', 'H', 'N', 'D'],
           ['V', 'U', 'F', 'U'],
           ['H', 'O', 'A', 'V']]

def test_path_legal():
    path1 = [(0,0),(0,1)]
    assert path_is_legal(path1, board_1) is True

    path2 = [(0, 0), (2, 1)]
    assert path_is_legal(path2, board_1) is False

    path3 = [(0, 0), (0, 0)]
    assert path_is_legal(path3, board_1) is False

    path4 = [(0, 0), (0, 1), (1,2)]
    assert path_is_legal(path4, board_1) is True

    path5 = [(0, 0), (1, 1), (2,2), (3,3)]
    assert path_is_legal(path5, board_1) is True

    path6 = [(0, 0), (1, 1), (2, 2), (3, 3), (4,4)]
    assert path_is_legal(path6, board_1) is False


def test_word_from_path():
    path1 = [(0, 0), (0, 1)]
    assert word_from_path(path1, board_1) == "TH"

    path2 = [(0, 0), (0, 1), (0,2), (0,3)]
    assert word_from_path(path2, board_1) == "THET"

    path3 = [(0, 0), (1, 0), (2, 0), (3, 0)]
    assert word_from_path(path3, board_1) == "TOVH"


def test_count_double():
    assert count_doubles_in_board(board_1) == 0

    board_2 = [['TH', 'H', 'E', 'T'],
               ['O', 'H', 'N', 'D'],
               ['VT', 'U', 'F', 'U'],
               ['H', 'O', 'A', 'V']]

    assert count_doubles_in_board(board_2) == 2