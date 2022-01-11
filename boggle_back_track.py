def old_worm_walking(t_rows: int, t_cols: int, index: int, pos_moves: list, all_paths: list, cur_path: list, req_len: int, lst_all_cells: list):
    # list cells [0, 1, 2, ..., 16]
    # possible_ moves [1, -1, +row_lem, -row_len, -row+1]

    if lst_all_cells[index] is None:  # todo - make sure its right
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
            if new_index < 0 or new_index > len(lst_all_cells) or lst_all_cells[new_index] is None:
                continue
            else:
                cur_path.append(lst_all_cells[new_index])
                lst_all_cells[new_index] = None
                worm_walking(t_rows, t_cols, new_index, pos_moves, all_paths, cur_path, req_len, lst_all_cells)
                return
    # cut_row, cur_col = (index // t_cols), (index % t_cols)


def worm_walking(t_rows: int, t_cols: int, index: int, pos_moves: list, all_paths: list, cur_path: list, req_len: int, lst_all_cells: list):
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
                finishd = worm_walking(t_rows, t_cols, new_index, pos_moves, all_paths, cur_path, req_len, lst_all_cells)
            else:
                return

        last_item = cur_path.pop()
        lst_all_cells[last_item] = last_item


def move_ok(new_index, all_cells_content) -> bool:
    if new_index < 0 or new_index > len(all_cells_content) or all_cells_content[new_index] is None:
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

    worm_walking(4,4, 0, pos_moves,lst_all_paths, [], 4, all_cell)

    print(lst_all_paths)
