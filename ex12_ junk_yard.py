import boogle
from typing import List, Tuple, Dict
import itertools


def is_valid_path(board, path, words):
    """
    check if a given path is legal and the corresponding word
    from the board is in the words list
    :param board: game board
    :param path: list of tuples
    :param words: iterable of all the words
    :return: if the path is legal and the word is in the word bank - returns
            the word, else - returns None
    """
    if path_is_legal(path, board):
        the_word = word_from_path(path, board)
        if the_word in words:
            return the_word


def word_from_path(path, board) -> str:  # todo - make sure you check the path is leggal before use
    """
    returns the string representing a word build from a given path
    :param path: list of tuples
    :param board: list of lists
    :return: string - the word
    """
    full_word = ""
    for cell_tuple in path:
        cur_row, cur_col = cell_tuple
        current_char = board[cur_row][cur_col]
        full_word += current_char

    return full_word


def path_is_legal(path, board) -> bool:
    """
    check if a given path is legal - no tuple is outside the board, all tuples
    are one next to the other and that there are no double tuples
    :param path: list of tuples representing the path of given word
    :param board: the game board - list of lists - so that we will measure its sizr
    :return: True - if legal, False - if not
    """
    num_rows = len(board)
    num_cols = len(board[0])

    prev_col = None
    prev_row = None

    if are_there_duplicates(path):
        return False
    for cell_tuple in path:
        cur_row, cur_col = cell_tuple
        # check all cells are in the board
        if cur_row < 0 or cur_col < 0 or cur_row > num_rows - 1 or cur_col > num_cols - 1:
            return False
        if prev_row is not None:
            if abs(cur_row-prev_row) > 1 or abs(cur_col - prev_col) > 1:
                return False
        prev_row = cur_row
        prev_col = cur_col
    return True


def find_length_n_paths(n, board, words):
    """
    1. normalize everything so i can use it
    2. build tuple locations in board
    3. create all combinations in the length of n
    4. filter out the combinations that aren't valid routes
    5. filter out all of the combinations that aren't in the words list
    6. return final list
    :param n:
    :param board:
    :param words: words dict
    :return:
    """
    # get list of all the tuples in the board
    all_board_locations = boogle.get_all_locations(board)
    # all possible paths in the length of n
    # todo - build something better - maybe recursion
    paths_combinations = list(itertools.combinations(all_board_locations, n))
    valid_paths = []
    for path in paths_combinations:
        if path_is_legal(path, board) and word_from_path(path, board) in words:
            valid_paths.append(path)

    return valid_paths


def find_length_n_words(n, board, words):
    """
    all the valid paths that create words in the length of n and are in the
    words list
    :param n: the desired word length
    :param board: the current board
    :param words: list of all words
    :return: list of all the valid paths
    """
    # get list of all the tuples in the board
    list_all_board_locations = boogle.get_all_locations(board)
    # counts how many cubes there are with two letters
    num_double_cubes = count_doubles_in_board(board)
    valid_paths = []

    # we want the path length to be corresponding with the number of doubled cubes
    for num_comb in range(n - num_double_cubes, n + 1):
        paths_combinations = list(itertools.combinations(list_all_board_locations, num_comb))

        for cur_path in paths_combinations:
            if path_is_legal(cur_path, board):
                cur_word = word_from_path(cur_path, board)
                if len(cur_word) == n and cur_word in words:
                    valid_paths.append(list(cur_path))

    return valid_paths


def count_doubles_in_board(board):
    """
    counts the number of double letter cubes in a given board
    :param board: the board
    :return: if all are single letters - 0
    """
    all_letters_str = ""
    num_cells = 0

    for cur_row in board:

        for cur_cell in cur_row:
            num_cells += 1
            all_letters_str += cur_cell

    num_letters = len(all_letters_str)
    return num_letters - num_cells


def max_score_paths(board, words):

    pass


def are_there_duplicates(given_list) -> bool:
    """
    checks if there are values that appear twice in a given list
    :param given_list: the list
    :return: True - if there is a double, False - if there isn't
    """
    there_are_double = False
    list_as_set = set(given_list)
    for item in given_list:
        if item in list_as_set:
            list_as_set.remove(item)
        else:
            there_are_double = True

    return there_are_double


# words_dict  - dict{key = length of word,value = list of dicts {eache first letter: all the words in the length}}

# [['T', 'H', 'E', 'T'],
#  ['O', 'H', 'N', 'D'],
#  ['V', 'U', 'F', 'U'],
#  ['H', 'O', 'A', 'V']


def find_length_n_paths(n, board, words):
    final_list = []
    all_loc = list_all_locations(board)

    num_cells = len(board) * len(board[0])
    if n > num_cells or n == 0:
        return final_list

    for start_locatin in all_loc:
        temp_list = [start_locatin]
        helper_length_n_paths(final_list, temp_list, n, board, start_locatin, words)
    return final_list


def helper_length_n_paths(all_paths: list, cur_path: list, req_len: int, board, last_cell: tuple, all_words):

    if len(cur_path) == req_len:
        cur_word = word_from_path(cur_path, board)
        if cur_word in all_words:
            all_paths.append(cur_path[::])

        return

    else:
        for neighbor in NEIGHBORS:
            new_row, new_col = add_location_tuples(last_cell, neighbor)
            location_tuple = tuple((new_row, new_col))
            if location_in_limits(new_row, new_col, board) and location_tuple not in cur_path:
                cur_path.append(location_tuple)
                helper_length_n_paths(all_paths, cur_path, req_len, board, location_tuple, all_words)
                cur_path.pop()
        return



# def helper_length_n_paths(all_paths: list, cur_path: list, req_len: int, board, last_cell: tuple, all_words):
#
#     if len(cur_path) == req_len:
#         cur_word = word_from_path(cur_path, board)
#         if cur_word in all_words:
#             all_paths.append(cur_path[::])
#
#         return
#
#     else:
#         for neighbor in NEIGHBORS:
#             new_row, new_col = add_location_tuples(last_cell, neighbor)
#             location_tuple = tuple((new_row, new_col))
#             if location_in_limits(new_row, new_col, board) and location_tuple not in cur_path:
#                 cur_path.append(location_tuple)
#                 helper_length_n_paths(all_paths, cur_path, req_len, board, location_tuple, all_words)
#                 cur_path.pop()
#         return


def get_all_locations(board):
    rows = len(board)
    cols = len(board[0])
    return [(x, y) for x in range(cols) for y in range(rows)]



def dict_words_game(file_path):
    """
    creats a dict of dicts - first key is the length of the word,
    second key is the first char of the word and then you'll reach a list
    of all the words in the given length, starting with the relevant char
    :param file_path: path to file txt with all the words
    :return: dict
    """
    final_dict = {}
    list_words = list_from_file(file_path)
    for word in list_words:
        word_length = len(word)
        first_char = word[0]
        if word_length not in final_dict:
            final_dict[word_length] = {}

        dict_by_len = final_dict[word_length]
        if first_char not in dict_by_len:
            dict_by_len[first_char] = []

        dict_char_and_len = dict_by_len[first_char]
        dict_char_and_len.append(word)

    return final_dict


def old_worm_walking(t_rows: int, t_cols: int, index: int, pos_moves: list,
                     all_paths: list, cur_path: list, req_len: int,
                     lst_all_cells: list):
    if lst_all_cells[index] is None:
        return False

    if len(cur_path) == req_len:
        cur_path.append(lst_all_cells[index])
        lst_all_cells[index] = None
        copied_path = cur_path[::]
        all_paths.append(copied_path)
        # revert to old version
        old_val = cur_path.pop()
        lst_all_cells[old_val] = old_val
        return

    else:
        cur_path.append(lst_all_cells[index])
        lst_all_cells[index] = None
        for move in pos_moves:
            new_index = index + move
            if new_index < 0 or new_index > len(lst_all_cells) or \
                    lst_all_cells[new_index] is None:
                continue
            else:
                cur_path.append(lst_all_cells[new_index])
                lst_all_cells[new_index] = None
                worm_walking(t_rows, t_cols, new_index, pos_moves, all_paths,
                             cur_path, req_len, lst_all_cells)
                return


def worm_walking(t_rows: int, t_cols: int, index: int, pos_moves: list,
                 all_paths: list, cur_path: list, req_len: int,
                 lst_all_cells: list):
    # list cells [0, 1, 2, ..., 16]
    # possible_ moves [1, -1, +row_lem, -row_len, -row+1]

    if len(cur_path) == req_len and cur_path not in all_paths:
        copied_path = cur_path[::]
        all_paths.append(copied_path)
        last_item = cur_path.pop()
        lst_all_cells[last_item] = last_item
        return True

    else:
        # add the current to list
        cur_path.append(index)
        lst_all_cells[index] = None

        for move in pos_moves:
            new_index = index + move
            if move_ok(new_index, all_cell):
                finishd = worm_walking(t_rows, t_cols, new_index, pos_moves,
                                       all_paths, cur_path, req_len,
                                       lst_all_cells)
            else:
                return

        last_item = cur_path.pop()
        lst_all_cells[last_item] = last_item


def move_ok(new_index, all_cells_content) -> bool:
    if new_index < 0 or new_index > len(all_cells_content) or \
            all_cells_content[new_index] is None:
        return False
    else:
        return True


def possible_moves(board) -> list:
    """
    returns a list of all the possible moves for a given board as list.
    the moves are relevant for an index that runs throughout the board
    :param board: a board for reference
    :return: list of all the moves
    """
    num_rows = len(board)
    num_col = len(board[0])
    list_moves = []

    # right and left
    list_moves.append(1)
    list_moves.append(-1)

    # up and down
    list_moves.append(num_col)
    list_moves.append(num_col * -1)

    # diagnol
    list_moves.append(num_col + 1)
    list_moves.append((num_col * -1) + 1)
    list_moves.append(num_col - 1)
    list_moves.append((num_col * -1) - 1)

    return list_moves


if __name__ == '__main__':

    b1 = [['T', 'H', 'E', 'T'],
          ['O', 'H', 'N', 'D'],
          ['V', 'U', 'F', 'U'],
          ['H', 'O', 'A', 'V']]

    pos_moves = possible_moves(b1)

    lst_all_paths = []
    all_cell = []
    for i in range(16):
        all_cell.append(i)

    worm_walking(4, 4, 0, pos_moves, lst_all_paths, [], 4, all_cell)

    print(lst_all_paths)
