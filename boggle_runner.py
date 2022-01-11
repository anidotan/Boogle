import time
from boggle_be import Boogle_brain
from boggle_board_randomizer import randomize_board
from boggle import list_from_file
from boggle_fe import Boogle_GUI
from typing import Callable, Tuple, List, Dict
import datetime

# decide the time of the game in seconds
GAME_TIME = 180
# get a list of all the words
words_list = list_from_file("boggle_dict.txt")

# every button has a func from the logic - needs a gui and a


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

        end_word_action = self.create_finished_word_action()
        self._gui.set_button_command('end_word', end_word_action)
        self._gui.set_score(self._brain.get_score())

        start_game_action = self.create_start_game_action()
        self._gui.set_button_command('start_button', start_game_action)
        self._gui.update_message_box(self._brain.get_message())
        self._gui.set_score(0)
        self._start_time = None

        game_over_action = self.create_game_over_action()
        self._gui.set_button_command('game_over', game_over_action)
        # self.new_game()

        play_again_action = self.create_start_game_action()
        self._gui.set_button_command('play_again', play_again_action)
        # self._gui.set_score(0)
        self._gui.update_message_box(self._brain.get_message())
        # self._start_time = None

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

    def create_game_over_action(self) -> Callable[[], None]:
        def fun() -> None:
            self._gui.change_screen('game_over')
            self._brain.finished_word()
            self._board = randomize_board()
            self._gui.set_new_game(self._board)
        return fun
    """
    def create_play_again_action(self, button_name: str) -> Callable[[], None]:
        def fun() -> None:
            self._gui.change_screen('main_game')
        return fun
    """

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

    """
    # in the BE
    def connect_buttons(buttons):
        for b in buttons:
            # if enter button
            b.set_button_command(action)
    #        letter buttons
    # start
    # end round
    
        for button_loc in buttons:
            self.
    
        def create_button_action(self, button_text: str) -> Callable[[], None]:
            def fun() -> None:
                self._model.type_in(button_text)
                self._gui.set_display(self._model.get_display())
    
            return fun
        
    """


def run_single_game():
    # get a board
    new_board = randomize_board()
    # creat a game brain with the cur board and words list
    brain = Boogle_brain(new_board, words_list)
    # flag of the game
    game_finished = False
    # creat GUI
    game_gui = Boogle_GUI(new_board)

    while not game_finished:
        # start counter
        time_counter = time.perf_counter()
        # run until time is over
        if time_counter < GAME_TIME:
            # at the start of every round
            game_gui.color_picked_letters(brain.letters_colored_pressed())
            game_gui.color_optional_letters(brain.letter_optional_color())
            game_gui.set_score(brain.get_score())
            game_gui.set_time(convert_to_time(time_counter))
            game_gui.show_chosen_words(brain.get_words_detected_list())

            # location_pressed = game_gui.get_pressed_key() # get letter press
            # if location_pressed is not None:  # if a cube was chosen
            #     brain.letter_input(location_pressed)



            word_finished_flag = game_gui.get_word_ended()
            if word_finished_flag:
                brain.finished_word()


        else:
            game_finished = True
            print("finished")


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
    print("hey")


