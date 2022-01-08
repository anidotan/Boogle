from boogle_back_track import possible_moves


class Boogle_brain:

    def __init__(self, cur_board, words_list):
        self._board = cur_board
        self._cur_word = ""
        self._pressed_tuples = []
        self.last_press = None
        self._all_words_list = words_list
        self._words_found = []
        self._score = 0

    def letter_input(self, location: tuple[int, int]) -> bool:
        """
        adds a letter
        :param location: location of pressed key as a tuple
        :return: True - if successful, False - if input is illegal
        """
        cur_row, cur_col = location
        if not self._pressed_tuples:
            self._pressed_tuples.append(location)
            self.last_press = location
            self._cur_word += self._board[cur_row][cur_col]
            return True
        else:
            if not check_press_ok(self.last_press, location):
                return False
            else:
                self._cur_word += self._board[cur_row][cur_col]
                self.last_press = location
                self._pressed_tuples.append(location)
                return True

    def finished_word(self) -> bool:
        """
        check if the word is in the word list
        :return: True - if word is correct, False- the words is not in the dictionary
        """
        cur_word = self._cur_word
        self._cur_word = ""
        if cur_word in self._all_words_list:
            self._words_found.append(cur_word)
            self.last_press = None
            num_cubes = len(self._pressed_tuples)
            self._pressed_tuples = []
            self._score += num_cubes**2
            return True
        else:
            # todo - set the status again
            return False

    def letters_colored_pressed(self) -> list[tuple]:
        """

        :return: list of tuples of all the words that should be colored as pressed ones
        """
        return self._pressed_tuples

    def letter_optional_color(self) -> list[tuple]:
        """

        :return: list of tuples of all the letters that are
        """
        final_list = []
        all_surrounding_tuples = surrounding_tuples(self._board, self.last_press)
        for c_tuple in all_surrounding_tuples:
            if c_tuple not in self._pressed_tuples:
                final_list.append(c_tuple)

        return final_list

    def get_words_detected(self) -> list:
        """

        :return: a list of all the words that has been found so far
        """
        return self._words_found

    def get_score(self):
        return self._score


def check_press_ok(last_press, cur_press):
    cur_row, cur_col = cur_press
    last_row, last_col = last_press
    if abs(cur_row - last_row) > 1 or abs(cur_col - last_col) > 1:
        return False
    else:
        return True


def surrounding_tuples(board, cur_tuple) -> list:
    """

    :return: a list of all the tuples surrounding a given tuple
    """
    final_list = []
    cur_row, cur_col = cur_tuple
    t_rows = len(board)
    t_cols = len(board[0])

    list_possible_row = list_change_coor(cur_row)
    list_possible_col = list_change_coor(cur_col)

    for row in list_possible_row:
        if row < t_rows and row > -1:
            for col in list_possible_col:
                if col < t_cols and col > -1:
                    if col == cur_col and row == cur_row:
                        continue
                    else:
                        final_list.append(tuple((row, col)))

    return final_list


def list_change_coor(coor):
    """
    :param coor: current index of col or row
    :return: a list of all the possible index near by
    """
    jumps = [-1, 0, 1]
    list_possible = []

    for j in jumps:
        list_possible.append(coor + j)

    return list_possible

if __name__ == '__main__':

    b1 = [['T', 'H', 'E', 'T'],
          ['O', 'H', 'N', 'D'],
          ['V', 'U', 'F', 'U'],
          ['H', 'O', 'A', 'V']]

    print(surrounding_tuples(b1, (1,0)))