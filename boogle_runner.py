import time
from boogle_be import Boogle_brain
from boggle_board_randomizer import randomize_board
from boogle import list_from_file
from boogle_fe import Boogle_GUI
import datetime

# decide the ti,e of the game in seconds
GAME_TIME = 180
# get a list of all the words
words_list = list_from_file("boggle_dict.txt")


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
            game_gui.color_possible_letters(brain.letter_optional_color())
            game_gui.set_score(brain.get_score())
            game_gui.set_time(convert_to_time(time_counter))
            game_gui.show_chosen_words(brain.get_words_detected_list())


            location_pressed = game_gui.get_pressed_key() # get letter press
            if location_pressed is not None:  # if a cube was chosen
                brain.letter_input(location_pressed)



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


if __name__ == '__main__':
    run_single_game()

