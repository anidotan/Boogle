from boggle_be import Boogle_brain, list_from_file
from boggle_board_randomizer import randomize_board
from boggle_fe import Boogle_GUI
from typing import Callable, Tuple, List, Dict

# get a list of all the words
words_list = list_from_file("boggle_dict.txt")


class BoggleController:
    def __init__(self):
        self._board = randomize_board()

        self._gui = Boogle_GUI(self._board)
        self._brain = Boogle_brain(self._board, words_list)

        self.config_letter_actions()

        self._gui.update_message_box(self._brain.get_message())
        self._gui.set_score(0)

        # set end word action
        end_word_action = self.create_finished_word_action()
        self._gui.set_button_command('end_word', end_word_action)

        # set start game action
        start_game_action = self.create_start_game_action()
        self._gui.set_button_command('start_button', start_game_action)

        # set game over
        game_over_action = self.create_game_over_action()
        self._gui.set_button_command('game_over', game_over_action)

        # set play again action
        play_again_action = self.create_play_again_action()
        self._gui.set_button_command('play_again', play_again_action)

    def create_letter_action(self, button_loc: Tuple[int, int]) -> Callable[[], None]:
        def fun() -> None:
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
            self._gui.change_screen('main_game')
            self._gui.advance_timer()
            self.update_board()

        return fun

    def create_game_over_action(self) -> Callable[[], None]:
        def fun() -> None:
            self._gui.change_screen('game_over')
            self._brain.finished_word()
            self._gui.set_time("")

        return fun

    def create_play_again_action(self) -> Callable[[], None]:
        def fun() -> None:
            self.new_game()
            self.config_letter_actions()
            self.update_board()
            self._gui.reset_timer()
            self._gui.change_screen('main_game')
            self._gui.advance_timer()

        return fun

    def config_letter_actions(self):
        letters = self._gui.get_letters()
        # add action to each letter
        for letter_location in letters.keys():
            action = self.create_letter_action(letter_location)
            self._gui.set_letter_command(letter_location, action)

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

    def new_game(self):
        self._board = randomize_board()
        self._brain = Boogle_brain(self._board, words_list)
        self._gui.set_time("")
        self._gui.set_new_game(self._board)

    def run(self) -> None:
        self._gui.run()


def run_game():
    controller.run()


if __name__ == '__main__':
    controller = BoggleController()
    controller.run()
