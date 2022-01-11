import time
from boogle_be import Boogle_brain
from boggle_board_randomizer import randomize_board
from boogle import list_from_file
from boogle_fe import Boogle_GUI
from typing import Callable, Tuple, List, Dict


# decide the time of the game in seconds
GAME_TIME = 180
# get a list of all the words
words_list = list_from_file("boggle_dict.txt")


class BoggleController:
    def __init__(self):
        self._board = randomize_board()

        self._gui = Boogle_GUI(self._board)
        self._brain = Boogle_brain(self._board, words_list)

        letters = self._gui.get_letters()
        # add action to each letter
        for letter_location in letters.keys():
            action = self.create_letter_action(letter_location)
            self._gui.set_letter_command(letter_location, action)

        end_word_action = self.create_finished_word_action('end_word')
        self._gui.set_button_command('end_word', end_word_action)
        self._gui.set_score(self._brain.get_score())

        start_game_action = self.create_start_game_action('start_button')
        self._gui.set_button_command('start_button', start_game_action)
        self._gui.update_message_box(self._brain.get_message())
        self._gui.set_score(0)
        self._start_time = None

        game_over_action = self.create_game_over_action('game_over')
        self._gui.set_button_command('game_over', game_over_action)

    def create_letter_action(self, button_loc: Tuple[int,int]) -> Callable[[], None]:
        def fun() -> None:
            # self._brain.letter_input(button_loc)
            self._brain.letter_input(button_loc)
            self.update_board()

        return fun

    def create_finished_word_action(self) -> Callable[[], None]:
        def fun() -> None:
            self._brain.finished_word()
            self.update_board()
        return fun

    def create_start_game_action(self) -> Callable[[], None]:
        def fun() -> None:
            # self._brain.start_game()
            self._start_time = time.time()
            self._gui.change_screen('main_game')
            self.update_board()
            # self._gui.change_to_main_screen()
        return fun

    def create_game_over_action(self, button_name: str) -> Callable[[], None]:
        def fun() -> None:
            self._gui.change_screen('game_over')
            self._brain.finished_word()
            self._board = randomize_board()
        return fun

    def update_board(self):
        self._gui.update_chosen_words(self._brain.get_words_detected_list())
        self._gui.set_score(self._brain.get_score())
        self._gui.update_message_box(self._brain.get_message())
        clicked_set = self._brain.letters_colored_pressed()
        if clicked_set:
            self._gui.color_picked_letters(clicked_set)
            set_of_disabled = self._brain.get_disabled_buttons()
            set_of_optional = self._brain.letter_optional_color()
            self._gui.color_optional_letters(set_of_optional)
            relevant_to_disable = set_of_disabled - set_of_optional
            self._gui.color_disabled_letters(relevant_to_disable)
        else:
            self._gui.reactivate_all_buttons()

    def update_time(self):
        cur_time = time.time()
        self._gui.set_time(convert_to_time(cur_time - self._start_time))

    def new_game(self):
        self._board = randomize_board()
        self._brain = Boogle_brain(self._board, words_list)

    def run(self) -> None:
        self._gui.run()


def convert_to_time(seconds):
    """
    :param seconds: number of seconds as float
    :return: the time in minutes and seconds as str MM:SS
    """
    seconds = seconds % (24 * 3600)

    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

def run_game():
    controller.run()


if __name__ == '__main__':
    # run_single_game()
    controller = BoggleController()
    controller.run()


