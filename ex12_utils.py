NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]


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
    return None


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


def word_from_path(path, board) -> str:
    """
    returns the string representing a word build from a given path
    :param path: list of tuples - make sure the path is legal
    :param board: list of lists
    :return: string - the word
    """
    full_word = ""
    for cell_tuple in path:
        cur_row, cur_col = cell_tuple
        current_char = board[cur_row][cur_col]
        full_word += current_char

    return full_word


def find_length_n_paths(n, board, words):
    """
    finds all the paths in length n that give out ords that are in the words list
    :param n: desired length of the path
    :param board: given board
    :param words: iterable of words
    :return: list of paths that are in length n
    """
    final_list = []
    all_loc = list_all_locations(board)

    num_cells = len(board) * len(board[0])
    if n > num_cells or n == 0:
        return final_list

    for start_locatin in all_loc:
        temp_list = [start_locatin]
        helper_length_n(final_list, temp_list, n, board, start_locatin,words, True, words)
    return final_list


def list_all_locations(board):
    """
    creates a list of tuples of all the locations in the board (row,col)
    :param board: given board
    :return: the list
    """
    rows = len(board)
    cols = len(board[0])
    return [(x, y) for x in range(cols) for y in range(rows)]


def location_in_limits(row, col, board) -> bool:
    """
    checks if a given row and col will give a cell that is in the limits of
    a given board
    :param row: given row
    :param col: given col
    :param board: the board
    :return: True - if the cell will be inside the board
             False - if the cell will be outside

    """
    num_rows = len(board)
    num_cols = len(board[0])
    if row < 0 or col < 0 or row > num_rows - 1 or col > num_cols - 1:
        return False
    else:
        return True


def add_location_tuples(tup1, tup2):
    """
    :param tup1: tuple of (row,col)
    :param tup2: tuple of (row,col)
    :return: the new row and col
    """
    cur_row, cur_col = tup1
    row_jump, col_jump = tup2
    new_row = cur_row + row_jump
    new_col = cur_col + col_jump
    return new_row, new_col


def find_length_n_words(n, board, words):
    """
    finds all the paths that give a legal word in length n
    :param n: desired length of the word
    :param board: given board
    :param words: iterable of words
    :return: list of paths that give out words that will be in the length of n
    """
    final_list = []
    all_loc = list_all_locations(board)

    num_cells = len(board) * len(board[0])
    if n > num_cells or n == 0:
        return final_list

    for start_locatin in all_loc:
        temp_list = [start_locatin]
        helper_length_n(final_list, temp_list, n, board, start_locatin, words, False, words)

    return final_list


def helper_length_n(all_paths: list, cur_path: list, req_len: int, board, last_cell: tuple, all_words, stop_parameter: bool, updated_word_list):
    """
    helps to get disired path that gives out a legal path or word
    in the length of n. works in recorsion
    :param all_paths: ,aster list of paths that will recive into it all the relevant paths
    :param cur_path: a current path that is built
    :param req_len: the desired len of the word
    :param board: given board
    :param last_cell: the last cell the has been added - default is the first cell
    :param all_words: iterable of all the words
    :param stop_parameter: True - according to path size, False - according to word size
    :return: nothing to return
    """

    relevant_len = get_length(cur_path, board, stop_parameter)
    if not updated_word_list:
        return
    if relevant_len == req_len:
        cur_word = word_from_path(cur_path, board)
        if cur_word in all_words:
            all_paths.append(cur_path[::])
            return
    elif relevant_len > req_len:
        return

    else:
        for neighbor in NEIGHBORS:
            new_row, new_col = add_location_tuples(last_cell, neighbor)
            location_tuple = tuple((new_row, new_col))
            if location_in_limits(new_row, new_col, board) and location_tuple not in cur_path:
                cur_path.append(location_tuple)
                helper_length_n(all_paths, cur_path, req_len, board, location_tuple, all_words,stop_parameter, minimize_words(word_from_path(cur_path,board),updated_word_list))
                cur_path.pop()
        return


def get_length(cur_path, board, stop_parameter: bool):
    """
    :param cur_path:
    :param board:
    :param stop_parameter: True - according to path size, False - according to word size
    :return: the relevant length
    """
    if stop_parameter:
        return len(cur_path)
    else:
        return len(word_from_path(cur_path, board))


def max_score_paths(board, words):
    """
    :param board: the current board
    :param words: iterable of all the legal words
    :return: list of all the paths with max score
        without double paths that give you the same word
    """
    number_all_cells = len(board) * len(board[0])
    dict_of_paths_by_len = creat_generic_dict(number_all_cells)
    list_paths = []
    all_loc = list_all_locations(board)
    for start_locatin in all_loc:
        temp_list = [start_locatin]
        cur_word = word_from_path(temp_list,board)
        rel_words = minimize_words(cur_word, words)
        helper_paths_with_dict(list_paths, temp_list, number_all_cells, board, start_locatin, words, True, dict_of_paths_by_len, rel_words, cur_word)
        list_paths.clear()

    list_to_return = all_score_paths(dict_of_paths_by_len, board)
    return list_to_return


def all_score_paths(dict_paths, board):
    """
    extract from dictionary of paths all the legal paths in the board without
    repeating the same words twice - if there are to ways to find a word it
    will give the longer version
    :param dict_paths: all paths in the board - categorized by length
    :param board: current board
    :return: list of all paths
    """
    list_words_found = []
    final_list_paths = []
    for i in range(16, 2 , -1):
        cur_paths_list = dict_paths[i]

        for cur_path in cur_paths_list:
            cur_word = word_from_path(cur_path, board)
            if cur_word not in list_words_found:
                list_words_found.append(cur_word)
                final_list_paths.append(cur_path)

    return final_list_paths


def minimize_words(cur_word, cur_list):
    """
    returns a relevant iterable of all the words that stars with a given starting word
    :param cur_word: the letters you want all the other words to start with
    :param cur_list: current iterable
    :return: a relevant iterable
    """
    rel_list = filter(lambda x: x.startswith(cur_word), cur_list)
    return list(rel_list)


def creat_generic_dict(num_index) -> dict:
    """
    create a generic dict of lists
    :param num_index: the greatest required key
    :return: dict of empty lists that the keys are from 3 to num_index
    """
    the_dict = {}
    for i in range(3, num_index + 1):
        the_dict[i] = []
    return the_dict


def helper_paths_with_dict(all_paths: list, cur_path: list, req_len: int, board, last_cell: tuple, all_words, stop_parameter: bool, dict_to_add, rel_words, cur_word):
    """
    :param all_paths: list of all the paths in the current length
    :param cur_path: the current path that is built
    :param req_len: the desired length
    :param board: current board
    :param last_cell: the last cell that had been added
    :param all_words: iterable of all the legal words
    :param stop_parameter: according to the type
    :param dict_to_add: the dictionary of all the paths in the board, catagorized by length
    :param rel_words: list of all the relevant words according to the current word that was created so far
    :param cur_word: the current word
    :return: none - adds the relevant to the dict without returning
    """
    relevant_len = get_length(cur_path, board, stop_parameter)

    if 2 < relevant_len and relevant_len <= req_len and word_from_path(cur_path, board) in all_words:
        add_path_to_dict(cur_path, dict_to_add)

    if not rel_words:
        return

    elif relevant_len == req_len:
        if cur_word in all_words:
            all_paths.append(cur_path[::])
            return
    elif relevant_len > req_len:
        return

    else:
        for neighbor in NEIGHBORS:
            new_row, new_col = add_location_tuples(last_cell, neighbor)
            location_tuple = tuple((new_row, new_col))
            if location_in_limits(new_row, new_col, board) and location_tuple not in cur_path:
                cur_word += board[new_row][new_col]
                cur_path.append(location_tuple)
                new_rel_words = minimize_words(cur_word, rel_words)
                helper_paths_with_dict(all_paths, cur_path, req_len, board, location_tuple, all_words, stop_parameter, dict_to_add, new_rel_words, cur_word)
                cur_path.pop()
                cur_word = cur_word[:-1]
        return


def add_path_to_dict(cur_path, dict_paths) -> None:
    """
    add a copy of a given path to a dict that is sorted according to the path length
    :param cur_path:
    :param dict_paths:
    :return: doesn't return anything
    """
    len_path = len(cur_path)
    cur_list_in_dict = dict_paths[len_path]
    cur_list_in_dict.append(cur_path[::])
