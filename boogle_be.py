SINGLE = None  # todo - define how i wannt it
DOUBLE = None


class Boogle_model:

    def __init__(self, cur_board, words_list):
        self._board = cur_board  # todo - do i need?
        self._cur_word = ""
        self._words_list = words_list

    def letter_pressed(self, letter: str, click_type):
        if click_type == SINGLE:
            self._cur_word += letter

        if click_type == DOUBLE:
            self._cur_word += letter




    def check_word(self):
        return self._cur_word in self._words_list
