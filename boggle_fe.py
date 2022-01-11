import tkinter as tk
from tkinter import font
from typing import Tuple, List, Callable, Set, Dict
from boggle_theme import *

DEFAULT_TIME = '03:00'


class Boogle_GUI:
    def __init__(self, board):
        self._board = board

        # build tkinter base
        self._root = tk.Tk()
        self._root.title('Welcome to Boogle!')
        self._root.geometry('500x600')
        self._root.configure(bg=DEFAULT_BG_COLOR)
        self._root.resizable(False, False)
        self._main_window = self._root
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_rowconfigure(0, weight=1)

        # general attributes
        self._letters: Dict[Tuple[int, int]: tk.Button] = {}
        self._time_left = 180
        self._buttons: Dict[str: tk.Button] = {}
        self._screens = {}
        self._current_screen = None
        self._boggle_img = tk.PhotoImage(file='./Boggle-logo.png')
        self._boggle_img_big = tk.PhotoImage(file='./Boggle-logo-big.png')
        self._timer_callback = None

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

        # build header
        self._header = tk.Frame()
        self._header_title = tk.Label(self._main_game_screen, image=self._boggle_img, bg=DEFAULT_BG_COLOR)
        self._header_title.grid(row=0, column=0, columnspan=10, rowspan=3, sticky=tk.S, pady=10)

        # build upper frame
        self._upper_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._upper_frame.grid(row=3, rowspan=2, column=0, columnspan=10, sticky=tk.N)

        # build middle frame
        self._middle_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._middle_frame.grid(row=5, rowspan=4, column=0, columnspan=10)

        # build bottom frame
        self._bottom_frame = tk.Frame(self._main_game_screen, bg=DEFAULT_BG_COLOR)
        self._bottom_frame.grid(row=9, rowspan=2, column=0, columnspan=10, sticky=tk.S)

        # build other sub-frames
        self.build_top_grid(self._upper_frame)
        self.build_middle_grid(self._middle_frame)
        self.build_side_grid(self._middle_frame)
        self.build_bottom_grid(self._bottom_frame)

    ######## BUILDERS ########
    def build_entrance_screen(self, parent: tk.Frame) -> None:
        """
        build the welcome frame
        """
        self._boogle_title = tk.Label(parent, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR, image=self._boggle_img_big,
                                      font=(FONT, 10, 'bold'))
        self._boogle_title.grid(row=0, column=0, columnspan=5, rowspan=5, sticky=tk.NSEW)
        self._secondary_title = tk.Label(parent, text='ARE YOU READY?!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                         font=(FONT, 15))
        self._secondary_title.grid(row=5, column=0, columnspan=5, pady=30, sticky=tk.NSEW)
        self._start_button = tk.Button(parent, text='START', bg=PRIMARY_BUTTON_COLOR, fg='black', width=9, height=2,
                                       activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 12, 'bold'))
        self._start_button.grid(row=7, column=2, sticky=tk.S, pady=20)
        self._buttons['start_button'] = self._start_button

    def build_game_over_screen(self, parent: tk.Frame) -> None:
        """
        build the game ended screen (game over)
        """
        self._screen_title = tk.Label(parent, text='Game Ended', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                      font=(FONT, 40, 'bold'))
        self._screen_title.grid(row=0, column=0, columnspan=5, pady=10, sticky=tk.NSEW)
        self._subtitle = tk.Label(parent, text='Good Job!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                  font=(FONT, 20))
        self._subtitle.grid(row=2, column=0, columnspan=5, pady=30, sticky=tk.NSEW)
        self._play_again_button = tk.Button(parent, text='Play Again', bg=PRIMARY_BUTTON_COLOR, fg='black', width=8,
                                            height=2,
                                            activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 10))
        self._play_again_button.grid(row=3, column=2, sticky=tk.S, pady=20)
        self._buttons['play_again'] = self._play_again_button

    def build_top_grid(self, parent: tk.Frame) -> None:
        """
        build the top grid
        """
        self._message_box = tk.Label(parent, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                     font=(FONT, 15, 'bold'))
        self._message_box.grid(row=0, rowspan=2, column=0, columnspan=10, sticky=tk.N)

    def build_middle_grid(self, parent: tk.Frame) -> None:
        """
        build middle grid - letters and timer
        """
        self._letter_board_contrainer = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        self._letter_board_contrainer.grid(row=0, column=0, columnspan=7, rowspan=4, padx=30, sticky=tk.E)
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(self._letter_board_contrainer, bg=DEFAULT_BG_COLOR, width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                label = f'{self._board[row][col]}'
                letter = self.create_button(cell, row, col, label)
                letter_loc = (row, col)
                self._letters[letter_loc] = letter

        self._time = tk.Label(parent, text=DEFAULT_TIME, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                              font=(FONT, 30, 'bold'))
        self._time.grid(row=4, column=5, columnspan=1, sticky=tk.W, rowspan=2, pady=10)

    def create_button(self, parent, row, col, label, rowspan=1, columnspan=1,
                      sticky=tk.NSEW) -> tk.Button:
        """
        create general button
        :param parent: tk.Frame
        :param row: int
        :param col: int
        :param label: str
        :param rowspan: int
        :param columnspan: int
        :param sticky: location (tk object)
        """
        button = tk.Button(parent, text=label, **BUTTON_STYLE)
        button.grid(row=row, column=col, pady=2, padx=2, rowspan=rowspan, columnspan=columnspan, sticky=sticky)
        return button

    def build_bottom_grid(self, parent: tk.Frame) -> None:
        """
        build bottom grid
        """
        self._end_game_button = tk.Button(parent, text='End Game', bg=PRIMARY_BUTTON_COLOR, fg='black', width=9,
                                          height=1,
                                          activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 9))
        self._end_game_button.grid(row=2, column=5, sticky=tk.S, pady=5)
        self._buttons['game_over'] = self._end_game_button
        self._footer = tk.Label(parent, text=f'Built by the awesome Zuk Arbell and Ani Dotan', bg=DEFAULT_BG_COLOR,
                                fg='white',
                                font=(FONT, 8))
        self._footer.grid(row=3, column=5, sticky=tk.S)

    def build_side_grid(self, parent: tk.Frame) -> None:
        """
        build bottom grid
        """
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

    ######## SETTERS ########
    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        """
        set the command the button is going to activate when pressed
        """
        self._buttons[button_name].configure(command=cmd)

    def set_letter_command(self, letter_loc: Tuple[int, int], cmd: Callable[[], None]) -> None:
        """
        set the command the letter button is going to activate when pressed
        """
        self._letters[letter_loc].configure(command=cmd)

    def color_picked_letters(self, letters_picked: List[Tuple[int, int]]) -> None:
        """
        color the picked letters on the board + make them un-clickable
        """
        for loc in letters_picked:
            self.color_button_by_loc(loc, LETTER_PICKED_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button)

    def color_disabled_letters(self, letters_disabled: Set[Tuple[int, int]]) -> None:
        """
        color the disabled (unreachable) letters on the board + make them un-clickable
        """
        for loc in letters_disabled:
            self.color_button_by_loc(loc, LETTER_DISABLED_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button)

    def color_optional_letters(self, optional_letters: List[Tuple[int, int]]) -> None:
        """
        color the optional letters on the board + make them clickable
        """
        for loc in optional_letters:
            self.color_button_by_loc(loc, LETTER_OPTION_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button, deactivate=False)

    def set_score(self, score: int) -> None:
        """
        set the shown score
        """
        self._score.configure(text=f'Score: {score}')

    def set_time(self, time: str) -> None:
        """
        update my timer attribute according to the time str
        """
        self._time.configure(text=time)

    def color_button_by_loc(self, button_loc: Tuple[int, int], new_color: str) -> None:
        """
        color the button by the location tuple
        """
        self._letters[button_loc].configure(bg=new_color)

    def color_button(self, button: tk.Button, new_color: str) -> None:
        """
        color the button by the given button object
        """
        button.configure(bg=new_color)

    def update_chosen_words(self, words: List[str]) -> None:
        """
        update the chosen words list
        """
        words_str = '\n'.join(words)
        self._chosen_words_box.configure(text=words_str)

    def update_message_box(self, message: str) -> None:
        """
        update the message box
        """
        self._message_box.configure(text=message)

    ######## GETTERS #######
    def get_letters(self):
        """
        :return: letters Dict
        """
        return self._letters

    def get_letter_loc(self, button: tk.Button) -> Tuple[int, int]:
        """
        :return: tuple representing the location on the button in the grid
        """
        for loc, letter in self._letters:
            if letter == button:
                return loc

    ######## EVENTS ########
    @staticmethod
    def deactivate_button(button: tk.Button, deactivate=True) -> None:
        """
        diactivate the given button, can activate as well (depends on the flag)
        """
        if deactivate:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def run(self) -> None:
        """
        run the mainloop
        """
        self._main_window.mainloop()

    def reset_timer(self, default_game_length: int = 180) -> None:
        """
        reset the timer according to the given game length
        """
        if self._timer_callback:
            self._root.after_cancel(self._timer_callback)

        self._timer_callback = None
        self._time_left = default_game_length
        time_left_str = self.sec_to_time_str(default_game_length)
        self.set_time(time_left_str)

    def advance_timer(self) -> None:
        """
        advance (or start) the timer by 1 sec
        """
        self._time_left -= 1
        if self._time_left <= 0:
            self.change_screen('game_over')
        else:
            time_left_str = self.sec_to_time_str(self._time_left)
            self.set_time(time_left_str)
            self._timer_callback = self._root.after(1000, self.advance_timer)

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

    def change_screen(self, new_screen_name: str):
        """
        cahnge the current screen to the new screen given in the params
        """
        self._current_screen.grid_remove()
        new_screen = self._screens[new_screen_name]
        self._current_screen = new_screen
        new_screen.grid(row=0, column=0, rowspan=11, columnspan=10)

    def reactivate_all_buttons(self) -> None:
        """
        reactivate all of the buttons on the board
        """
        for button in self._letters.values():
            if button['state'] != tk.NORMAL:
                self.deactivate_button(button, deactivate=False)
            self.color_button(button, LETTER_COLOR)

    def set_new_game(self, new_board):
        """
        set up a new game
        """
        self._board = new_board
        self._letters: Dict[Tuple[int, int]: tk.Button] = {}
        self.build_middle_grid(self._middle_frame)
        self.reset_timer()
