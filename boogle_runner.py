import time
from boogle_be import Boogle_brain
from boggle_board_randomizer import randomize_board
from boogle import list_from_file
from boogle_fe import Boogle_GUI
from typing import Callable, Tuple, List, Dict
import datetime

# decide the time of the game in seconds
GAME_TIME = 180
# get a list of all the words
words_list = list_from_file("boggle_dict.txt")

# every button has a func from the logic - needs a gui and a

# todo: letter input connect with each letter
# todo: connect finished word with tthe word ended


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
        self._gui.set_score(self._brain.get_score())

    def create_letter_action(self, button_loc: Tuple[int,int]) -> Callable[[], None]:
        def fun() -> None:
            self._brain.letter_input(button_loc)
            # todo: do we need to do the default score?
            print(f'button in location: {button_loc}')
            self._brain.letter_input(button_loc)
            self.update_board()

        return fun

    def create_finished_word_action(self, button_name: str) -> Callable[[], None]:
        def fun() -> None:
            self._brain.finished_word()
            self._gui.reactivate_buttons()
            print('word finished!')
            # todo: do we need to do anything else?
        return fun

    def update_board(self):
        self._gui.set_score(self._brain.get_score())
        self._gui.color_picked_letters(self._brain.letters_colored_pressed())
        self._gui.color_possible_letters(self._brain.letter_optional_color())


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
    # creat a game brain with the cur board and wrods list
    brain = Boogle_brain(new_board, words_list)
    # flag of the game
    game_finished = False
    # creat GUI todo
    game_gui = None

    while not game_finished:
        # start counter
        time_counter = time.perf_counter()
        # run untill time is over
        if time_counter < GAME_TIME:
            # at the start of every round
            cells_pressed = brain.letters_colored_pressed() # pressed letters and optional press
            optional_cells = brain.letter_optional_color()
            game_gui.color_press(cells_pressed)
            game_gui.optional_color(optional_cells)
            game_gui.show_score(brain.get_score())
            game_gui.show_time(convert_to_time(time_counter))
            game_gui.show_words(brain.get_words_detected())


            location_pressed = game_gui.get_press # get letter press
            if location_pressed is not None:  # if a cube was chosen
                brain.letter_input(location_pressed)
            full_word = game_gui.get_finish_words()
            if full_word is True:
                brain.finished_word()


        else:
            game_finished = True
            print("finished")


def convert_to_time(seconds):
    seconds = seconds % (24 * 3600)

    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)


if __name__ == '__main__':
    # run_single_game()
    controller = BoggleController()
    controller.run()


