import tkinter as tk
from tkinter import font
from typing import Optional, Tuple, List, Callable, Set
from boogle_theme import *

DEFAULT_TIME = '00:00'


class Boogle_GUI:
    def __init__(self, board):
        self.__board = board

        # build tkinter base
        self._root = tk.Tk()
        self._root.title('Welcome to Boogle!')
        self._root.geometry('500x500')
        self._root.configure(bg=DEFAULT_BG_COLOR)
        self._root.resizable(False, False)
        self._main_window = self._root
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_rowconfigure(0, weight=1)

        # general attributes
        self._time_left = 180
        self._letters = {}
        self._buttons = {}
        self._screens = {}
        self._current_screen = None

        # welcome screen
        self._welcome_screen = tk.Frame(self._root, bg=DEFAULT_BG_COLOR)
        self._welcome_screen.grid(row=0, column=0)
        self._screens['welcome_screen'] = self._welcome_screen
        self.build_entrance_screen(self._welcome_screen)
        self._current_screen = self._welcome_screen

        # game over screen
        self._game_over = tk.Frame(self._root, bg=DEFAULT_BG_COLOR)
        self.build_game_over_screen(self._game_over)
        self._screens['game_over'] = self._game_over

        # main game screen
        self._main_game_screen = tk.Frame(self._root, bg=DEFAULT_BG_COLOR)
        self._screens['main_game'] = self._main_game_screen

        # build upper frame
        self._upper_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._upper_frame.grid(row=0, rowspan=2, column=0, columnspan=10, sticky=tk.N)

        # build middle frame
        self._middle_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._middle_frame.grid(row=2, rowspan=6, column=0, columnspan=10)

        # build bottom frame
        self._bottom_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._bottom_frame.grid(row=8, rowspan=3, column=0, columnspan=10, sticky=tk.S, pady=10)

        # build other sub-frames
        self.build_top_grid(self._upper_frame)
        self.build_letter_grid(self._middle_frame)
        self.build_side_grid(self._middle_frame)
        self.build_bottom_grid(self._bottom_frame)

    ######## BUILDERS ########
    """
    def change_to_main_screen(self):
        # change the entrance screen to main game screen by removing and adding the objects to the grid
        for obj in self._welcome_screen_obj:
            obj.grid_remove()
        self._main_game_screen.grid(row=0, column=0, rowspan=10, columnspan=10)
    
    """

    def change_screen(self, new_screen_name: str):
        self._current_screen.grid_remove()
        new_screen = self._screens[new_screen_name]
        self._current_screen = new_screen
        new_screen.grid(row=0, column=0, rowspan=10, columnspan=10)
        if new_screen_name == 'main_game':
            self.advance_timer()
            print('started timer after changing to main screen')
        elif new_screen_name == 'game_over':
            self.reset_timer()


    def build_entrance_screen(self, parent):
        self._boogle_title = tk.Label(parent, text='Welcome to Boogle!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                      font=(FONT, 30, 'bold'))
        self._boogle_title.grid(row=0, column=0, columnspan=5, pady=10, sticky=tk.NSEW)
        self._secondary_title = tk.Label(parent, text='ARE YOU READY?!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                         font=(FONT, 15))
        self._secondary_title.grid(row=2, column=0, columnspan=5, pady=30, sticky=tk.NSEW)
        self._start_button = tk.Button(parent, text='START', bg=PRIMARY_BUTTON_COLOR, fg='black', width=9, height=2,
                                       activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 12, 'bold'))
        self._start_button.grid(row=3, column=2, sticky=tk.S, pady=20)
        self._buttons['start_button'] = self._start_button

        # self._welcome_screen_obj.append(self._boogle_title)
        # self._welcome_screen_obj.append(self._secondary_title)
        # self._welcome_screen_obj.append(self._start_button)

    def build_game_over_screen(self, parent):
        self._screen_title = tk.Label(parent, text='Game Ended', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                      font=(FONT, 30, 'bold'))
        self._screen_title.grid(row=0, column=0, columnspan=5, pady=10, sticky=tk.NSEW)
        self._subtitle = tk.Label(parent, text='Good Job!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                         font=(FONT, 15))
        self._subtitle.grid(row=2, column=0, columnspan=5, pady=30, sticky=tk.NSEW)
        self._play_again_button = tk.Button(parent, text='Play Again', bg=PRIMARY_BUTTON_COLOR, fg='black', width=9, height=2,
                                       activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 10, 'bold'))
        # self._play_again_button.grid(row=3, column=2, sticky=tk.S, pady=20)
        self._buttons['play_again'] = self._play_again_button

    def build_top_grid(self, parent):
        self._message_box = tk.Label(parent, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                     font=(FONT, 15, 'bold'))
        self._message_box.grid(row=0, rowspan=2, column=0, columnspan=10, sticky=tk.N, pady=5)

    def reset_timer(self, default_game_length:int=180):
        self._time_left = default_game_length
        time_left_str = self.sec_to_time_str(default_game_length)
        self.set_time(time_left_str)

    def advance_timer(self):
        print('started timer')
        self._time_left -= 1
        if self._time_left <= 0:
            self.change_screen('game_over')
        else:
            time_left_str = self.sec_to_time_str(self._time_left)
            self.set_time(time_left_str)
            self._root.after(1000, self.advance_timer)


    def sec_to_time_str(self, seconds: int):
        """
        :param seconds: number of seconds as float
        :return: the time in minutes and seconds as str MM:SS
        """
        seconds = seconds % (24 * 3600)

        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%02d:%02d" % (minutes, seconds)


    def build_letter_grid(self, parent):
        self._letter_board_contrainer = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        self._letter_board_contrainer.grid(row=0, column=0, columnspan=7, rowspan=4, padx=30, sticky=tk.E)
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(self._letter_board_contrainer, bg=DEFAULT_BG_COLOR, width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                label = f'{self.__board[row][col]}'
                letter = self.create_button(cell, row, col, label)
                letter_loc = (row, col)
                self._letters[letter_loc] = letter

    def create_button(self, parent, row, col, label, rowspan: int = 1, columnspan: int = 1,
                      sticky=tk.NSEW) -> tk.Button:
        button = tk.Button(parent, text=label, **BUTTON_STYLE)
        button.grid(row=row, column=col, pady=2, padx=2, rowspan=rowspan, columnspan=columnspan, sticky=sticky)
        return button

    def build_bottom_grid(self, parent):
        self._time = tk.Label(parent, text=DEFAULT_TIME, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                              font=(FONT, 20))
        self._time.grid(row=0, column=5, columnspan=2, rowspan=2, pady=30)
        self._end_game_button = tk.Button(parent, text='End Game', bg=PRIMARY_BUTTON_COLOR, fg='black', width=8, height=1,
                                       activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 8))
        self._end_game_button.grid(row=2, column=5, sticky=tk.S)
        self._buttons['game_over'] = self._end_game_button
        self._footer = tk.Label(parent, text=f'Built by the awesome Zuk Arbell and Ani Dotan', bg=DEFAULT_BG_COLOR,
                                fg=FONT_COLOR,
                                font=(FONT, 8))
        self._footer.grid(row=3, column=5, sticky=tk.S)


    def build_side_grid(self, parent):
        self._side_frame = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        self._side_frame.grid(row=0, column=7, rowspan=3, columnspan=2)
        self._score = tk.Label(self._side_frame, text=f'Score:', fg=FONT_COLOR, bg=DEFAULT_BG_COLOR,
                               font=(FONT, 15, 'bold'))
        self._score.grid(row=0, column=0, rowspan=2)
        self._chosen_words_title = tk.Label(self._side_frame, text='Chosen Words:', fg=FONT_COLOR, bg=DEFAULT_BG_COLOR,
                                            font=(FONT, 12))
        self._chosen_words_title.grid(row=2, column=0, pady=5)
        self._chosen_words_box = tk.Label(self._side_frame, text='', bg=TEXTBOX_BG_COLOR, fg=FONT_COLOR,
                                          font=(FONT, 10, 'bold'), height=8, width=10)
        self._chosen_words_box.grid(row=3, column=0, rowspan=2, columnspan=3, pady=5)
        self._end_word = tk.Button(self._side_frame, text='END WORD', bg=PRIMARY_BUTTON_COLOR, fg='black', width=12,
                                   height=1,
                                   activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 9))
        self._end_word.grid(row=6, pady=10)
        self._buttons['end_word'] = self._end_word

    ######## SETTERS / PROP UPDATES ########
    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def set_letter_command(self, letter_loc: Tuple[int, int], cmd: Callable[[], None]):
        self._letters[letter_loc].configure(command=cmd)

    def color_picked_letters(self, letters_picked: List[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_picked:
            self.color_button_by_loc(loc, LETTER_PICKED_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button)

    def color_disabled_letters(self, letters_disabled: Set[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_disabled:
            self.color_button_by_loc(loc, LETTER_DISABLED_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button)

    def reactivate_all_buttons(self):
        for button in self._letters.values():
            if button['state'] != tk.NORMAL:
                self.deactivate_button(button, deactivate=False)
            self.color_button(button, LETTER_COLOR)

        # todo: maybe use this https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/

    def color_optional_letters(self, optional_letters: List[Tuple[int, int]]):
        # color the letters on the board
        for loc in optional_letters:
            self.color_button_by_loc(loc, LETTER_OPTION_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button, deactivate=False)

    def set_score(self, score: int):
        # self.__score = score
        self._score.configure(text=f'Score: {score}')

    def set_time(self, time: str):
        # get the time, update my timer attribute
        # todo: change the way set score is
        self._time.configure(text=time)

    def color_button_by_loc(self, button_loc, new_color):
        self._letters[button_loc].configure(bg=new_color)

    def color_button(self, button, new_color):
        button.configure(bg=new_color)

    def set_word_ended(self):
        # todo: doesn't change the word on the screen
        # todo: only run when key is pressed. add an event of clicked on button - end
        self.__word_ended = True

    # todo: REMOVE?

    def update_chosen_words(self, words: List[str]):
        # show the chosen words
        words_str = '\n'.join(words)
        self._chosen_words_box.configure(text=words_str)

    #     todo: update the panel

    def update_message_box(self, message: str):
        # update the message box (error, congrats, etc)
        self._message_box.configure(text=message)

    def set_current_key(self, key):
        self.__current_key = key
        # print(f'key clicked: {type(self.__current_key)}')

    #     todo: remove this and move it to the logic

    ######## GETTERS #######
    def get_word_ended(self):
        word_ended_flag = False
        if self.__word_ended:
            word_ended_flag = self.__word_ended
            self.__word_ended = False
            self.reactivate_all_buttons()
        return word_ended_flag

    # todo: move to the logic

    def get_pressed_key(self) -> Optional[Tuple[int, int]]:
        cur_key = self.__current_key
        self.__current_key = None
        return cur_key

    def get_letters(self):
        return self._letters

    def get_letter_loc(self, button):
        for loc, letter in self._letters:
            if letter == button:
                return loc

    ######## EVENTS ########
    def deactivate_button(self, button: tk.Button, deactivate=True):
        if deactivate:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def run(self) -> None:
        self._main_window.mainloop()
