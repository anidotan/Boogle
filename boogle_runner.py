import time
from boogle_be import Boogle_brain
from boggle_board_randomizer import randomize_board
from boogle import list_from_file
import datetime

# decide the ti,e of the game in seconds
GAME_TIME = 180
# get a list of all the words
words_list = list_from_file("boggle_dict.txt")


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
    run_single_game()

