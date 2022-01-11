class Boogle_brain:

    def __init__(self, cur_board, words_list):
        self._board = cur_board
        self._cur_word = ""
        self._pressed_tuples = set()
        self._possible_moves = set()
        self._disabled_buttons = set()
        self._last_press = None
        self._all_words_list = words_list
        self._words_found = []
        self._score = 0
        self._message = None

    def letter_input(self, location: tuple[int, int]) -> bool:
        """
        adds a letter, updates the current word that is built, and the list of
        pressed buttons and the buttons that should be disabled
        :param location: location of pressed key as a tuple
        :return: True - if successful, False - if input is illegal
        """
        cur_row, cur_col = location
        # if nothing is pressed yet
        if not self._pressed_tuples:
            self._pressed_tuples.add(location)
            self._last_press = location
            self._cur_word += self._board[cur_row][cur_col]
            self._disabled_buttons = all_locations_as_set(self._board)
            self._disabled_buttons.remove(location)
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
        activate a sequence of actions when player declair he finished a word:
        - resets current word
        - reset last key pressed
        - reset the list of pressed buttons and buttons to disable
        - updates the score and the relevant message that will be displayed later
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
            if cur_word not in self._words_found:
                # add the score and board
                self._words_found.append(cur_word)
                self._score += num_cubes**2
                # self._message = "you're word was correct!\nyou gained " + str(num_cubes**2) + " points"
                self._message = "your word was correct!"
            else:
                # self._message = "you already found this word,\ntry a different one"
                self._message = "you already found this word, please try a different one"
            return True
        else:
            self._message = "sorry! that's not a word"
            return False

    def letters_colored_pressed(self) -> set:
        """
        :return: set of tuples of all the words that should be colored as pressed ones
        """
        return self._pressed_tuples

    def letter_optional_color(self) -> set[tuple]:
        """
        :return: set of tuples of all the letters that are optional to choose from
        """
        final_set = set()
        if self._last_press is None:
            return final_set
        else:
            all_surrounding_tuples = surrounding_tuples(self._board, self._last_press)
            for c_tuple in all_surrounding_tuples:
                if c_tuple not in self._pressed_tuples:
                    final_set.add(c_tuple)

            return final_set

    def get_disabled_buttons(self):
        """
        :return: a set of all the tuples that aren't the ones who have been pressed by now
        """
        return self._disabled_buttons

    def get_words_detected_list(self) -> list:
        """
        :return: a list of all the words that has been found so far
        """
        return self._words_found

    def get_score(self):
        """
        :return: the current score in the game
        """
        return self._score

    def get_message(self):
        """
        :return: the message, could be:
        - success in finding a word
        - remark that the word has been found already
        - remark that the guessed word is wrong
        - default - wish the player "have fun!"
        """
        temp = self._message
        self._message = None
        if not temp:
            temp = "Have fun!"

        return temp


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
    """
    :param board:
    :return: al the possible indexes of a given board as a set of tuples
    """
    final = set()
    rows = len(board)
    cols = len(board[0])
    for x in range(cols):
        for y in range(rows):
            final.add(tuple((x, y)))

    return final

