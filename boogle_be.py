from boogle_back_track import possible_moves
from boogle import get_all_locations

class Boogle_brain:

    def __init__(self, cur_board, words_list):
        self._board = cur_board
        self._cur_word = ""
        self._pressed_tuples = set()
        self._possible_moves = set()
        self._disabled_buttons = set()
        self.last_press = None
        self._all_words_list = words_list
        self._words_found = []
        self._score = 0

    def __str__(self):  # remove
        total = ""
        for row in self._board:
            total = total + str(row) + "\n"
        return total

    def letter_input(self, location: tuple[int, int]) -> bool:
        """
        adds a letter
        :param location: location of pressed key as a tuple
        :return: True - if successful, False - if input is illegal
        """
        cur_row, cur_col = location
        if not self._pressed_tuples:
            self._pressed_tuples.add(location)
            self._last_press = location
            self._cur_word += self._board[cur_row][cur_col]
            all_tuples = all_locations_as_set(self._board)
            self._disabled_buttons = all_tuples.remove(location)
            return True
        else:
            if not check_press_ok(self._last_press, location):  # todo - maybe i can delete this
                return False
            else:
                self._cur_word += self._board[cur_row][cur_col]
                self._last_press = location
                self._pressed_tuples.add(location)
                self._disabled_buttons.remove(location)
                return True

    def finished_word(self) -> bool:
        """
        check if the word is in the word list
        :return: True - if word is correct, False- the words is not in the dictionary
        """
        cur_word = self._cur_word
        num_cubes = len(self._pressed_tuples)
        # reset the local variables
        self._cur_word = ""
        self._last_press = None
        self._pressed_tuples.clear()
        self._disabled_buttons.clear()

        if cur_word in self._all_words_list:
            # add the score and board
            self._words_found.append(cur_word)
            self._score += num_cubes**2
            return True
        else:
            return False
        # todo - add somthing to ahppen when the word is wrong

    def letters_colored_pressed(self) -> list[tuple]:
        """
        :return: list of tuples of all the words that should be colored as pressed ones
        """
        return self._pressed_tuples

    def letter_optional_color(self) -> list[tuple]:
        """
        :return: list of tuples of all the letters that are optional to choose from
        """
        final_list = []
        all_surrounding_tuples = surrounding_tuples(self._board, self._last_press)
        for c_tuple in all_surrounding_tuples:
            if c_tuple not in self._pressed_tuples:
                final_list.append(c_tuple)

        return final_list

    def get_words_detected_list(self) -> list:
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


def all_locations_as_set(board):
    final = set()
    rows = len(board)
    cols = len(board[0])
    for x in range(cols):
        for y in range(rows):
            final.add(tuple((x, y)))

    return final

if __name__ == '__main__':

    b1 = [['T', 'H', 'E', 'T'],
          ['O', 'H', 'N', 'D'],
          ['V', 'U', 'F', 'U'],
          ['H', 'O', 'A', 'V']]

    print(all_locations_as_set(b1))
    # list = ["THE"]
    # brain = Boogle_brain(b1, list)
    # for i in range(3):
    #     print(brain.get_words_detected_list())
    #     print(brain.letters_colored_pressed())
    #     x = input("type x")
    #     y= input("y")
    #     z = tuple((int(x),int(y)))
    #     print(z)
    #     brain.letter_input(z)
    #     # brain.letter_input((0, 1))
    #     # brain.letter_input((0,2))
    # brain.finished_word()
    # print(brain.get_words_detected_list())
    # print(brain.letters_colored_pressed())